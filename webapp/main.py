"""BugHunter Web — scan a GitHub repo from the browser.

Phase 1 (land & expand): free scans, per-IP daily limit, no registration.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
import time
import uuid
from collections import defaultdict
from pathlib import Path

from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

from bug_hunter.scanner import scan_project, get_project_stats
from bug_hunter.analyzer.static import StaticAnalyzer
from bug_hunter.analyzer.ast_analyzer import ASTAnalyzer
from bug_hunter.analyzer.dedup import dedup_bugs
from bug_hunter.analyzer.base import AnalysisResult
from bug_hunter.ignore import IgnoreRules, apply_ignores

APP_DIR = Path(__file__).resolve().parent
REPORTS_DIR = APP_DIR / "reports"
REPORTS_DIR.mkdir(exist_ok=True)

DAILY_LIMIT = int(os.environ.get("BH_DAILY_LIMIT", "5"))
CLONE_TIMEOUT = 120  # seconds

app = FastAPI(title="BugHunter Web")
templates = Jinja2Templates(directory=str(APP_DIR / "templates"))

# {ip: [timestamps of today's scans]}
_usage: dict[str, list[float]] = defaultdict(list)


def _day_start() -> float:
    return time.time() - (time.time() % 86400)


def _check_limit(ip: str) -> int:
    """Return remaining scans today for this IP."""
    today = _day_start()
    _usage[ip] = [t for t in _usage[ip] if t >= today]
    return DAILY_LIMIT - len(_usage[ip])


def _record_scan(ip: str):
    _usage[ip].append(time.time())


def _clone_repo(url: str, dest: Path):
    subprocess.run(
        ["git", "clone", "--depth", "1", "--quiet", url, str(dest)],
        check=True, timeout=CLONE_TIMEOUT,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )


def _run_scan(project: Path) -> tuple[AnalysisResult, dict]:
    files = scan_project(project)
    stats = get_project_stats(files)
    result = AnalysisResult()
    result.merge(StaticAnalyzer().analyze(files))
    result.merge(ASTAnalyzer().analyze(files))
    result.bugs = dedup_bugs(result.bugs)
    ignore = IgnoreRules(project)
    file_lines = {str(f.relative_path): f.content.split("\n") for f in files}
    result.bugs = apply_ignores(result.bugs, ignore, file_lines)
    return result, stats


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    remaining = _check_limit(request.client.host)
    return templates.TemplateResponse("index.html", {
        "request": request, "remaining": remaining, "limit": DAILY_LIMIT,
    })


@app.post("/scan", response_class=HTMLResponse)
async def scan(request: Request, repo_url: str = Form(...)):
    ip = request.client.host
    if _check_limit(ip) <= 0:
        raise HTTPException(
            status_code=429,
            detail=f"Daily limit reached ({DAILY_LIMIT} scans/day). Come back tomorrow!",
        )

    repo_url = repo_url.strip()
    if not repo_url.startswith(("https://github.com/", "http://github.com/")):
        raise HTTPException(status_code=400, detail="Only https://github.com/ URLs are supported for now.")

    scan_id = uuid.uuid4().hex[:12]
    workdir = Path(tempfile.mkdtemp(prefix=f"bh_{scan_id}_"))
    try:
        _clone_repo(repo_url, workdir / "repo")
        result, stats = _run_scan(workdir / "repo")
        _record_scan(ip)

        sev_counts = {}
        for b in result.bugs:
            sev_counts[b.severity] = sev_counts.get(b.severity, 0) + 1

        top = [b for b in result.sorted_bugs() if b.severity in ("critical", "high")][:25]

        return templates.TemplateResponse("report.html", {
            "request": request,
            "repo_url": repo_url,
            "stats": stats,
            "sev_counts": sev_counts,
            "total": len(result.bugs),
            "top_bugs": top,
            "remaining": _check_limit(ip),
            "limit": DAILY_LIMIT,
        })
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=408, detail="Cloning took too long — repo may be huge.")
    except subprocess.CalledProcessError:
        raise HTTPException(status_code=400, detail="Could not clone. Check the URL and that the repo is public.")
    except Exception as e:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=f"Scan failed: {e}")
    finally:
        shutil.rmtree(workdir, ignore_errors=True)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
