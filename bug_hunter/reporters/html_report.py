from datetime import datetime
from pathlib import Path

from .. import reporters
from ..config import SEVERITY_ORDER

SEVERITY_WEIGHT = {"critical": 10, "high": 6, "medium": 3, "low": 1, "info": 0.5}
SEVERITY_LABEL = {"critical": "Critical", "high": "High", "medium": "Medium", "low": "Low", "info": "Info"}
SEVERITY_HEX = {
    "critical": "#d93025",
    "high": "#ea4335",
    "medium": "#f9ab00",
    "low": "#1a73e8",
    "info": "#5f6368",
}


def compute_score(result) -> tuple:
    """Return (score_0_100, grade_letter).

    Start at 100 and subtract severity-weighted points per finding. When there
    are no critical/high findings, cap the penalty so a few low/info nits don't
    crash the grade — scale those only by 0.9x their base weight.
    """
    bugs = result.bugs
    if not bugs:
        return 100, "A"

    critical_high = [b for b in bugs if b.severity in ("critical", "high")]
    if critical_high:
        total = sum(SEVERITY_WEIGHT.get(b.severity, 1) for b in bugs)
        raw = 100 - total
    else:
        # only medium/low/info findings: penalty is bounded (1.5x the low-band total)
        soft = sum(
            SEVERITY_WEIGHT.get(b.severity, 1)
            for b in bugs
            if b.severity in ("medium", "low", "info")
        )
        raw = max(100 - soft * 0.9, 62)

    score = round(min(100, max(0, raw)), 1)
    if score >= 95:
        grade = "A"
    elif score >= 85:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"
    return score, grade


def build_security_score_bars(result) -> str:
    counts = {s: 0 for s in SEVERITY_LABEL}
    for b in result.bugs:
        counts[b.severity] = counts.get(b.severity, 0) + 1
    total = max(1, sum(counts.values()))
    bars = []
    for sev, label in SEVERITY_LABEL.items():
        n = counts[sev]
        pct = n / total * 100
        bars.append(
            f'<div class="sev-row"><span class="sev-dot" style="background:{SEVERITY_HEX[sev]}"></span>'
            f'<span class="sev-label">{label}</span>'
            f'<div class="sev-bar"><div class="sev-fill" style="width:{pct:.1f}%;background:{SEVERITY_HEX[sev]}"></div></div>'
            f'<span class="sev-count">{n}</span></div>'
        )
    return "\n".join(bars)


def escape(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("\n", "<br>")
    )


def generate_html_report(result, project_path: str, project_stats: dict, analyzers_used: list[str]) -> Path:
    REPORT_DIR = reporters.REPORT_DIR  # noqa: F821
    REPORT_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    project_name = Path(project_path).name
    out_file = REPORT_DIR / f"security_review_{project_name}_{timestamp}.html"

    sorted_bugs = result.sorted_bugs()
    score, grade = compute_score(result)

    severity_counts = {}
    for b in sorted_bugs:
        severity_counts[b.severity] = severity_counts.get(b.severity, 0) + 1

    findings_html = []
    for b in sorted_bugs:
        hex_color = SEVERITY_HEX.get(b.severity, "#5f6368")
        label = SEVERITY_LABEL.get(b.severity, b.severity)
        snippet_html = ""
        if b.code_snippet:
            snippet_html = (
                f'<details><summary>Code</summary><pre class="code">{escape(b.code_snippet)}</pre></details>'
            )
        findings_html.append(
            f"""
            <div class="finding">
              <div class="finding-head">
                <span class="badge" style="background:{hex_color}">{label}</span>
                <span class="finding-title">{escape(b.title)}</span>
                <span class="conf">confidence {b.confidence:.0%}</span>
              </div>
              <div class="finding-meta">
                <code>{escape(b.file)}</code>:{b.line}
                <span class="analyzer">{escape(b.analyzer)}</span>
              </div>
              <div class="finding-desc"><b>Problem:</b> {escape(b.description)}</div>
              <div class="finding-fix"><b>Recommendation:</b> {escape(b.suggestion)}</div>
              {snippet_html}
            </div>
            """
        )

    languages = ""
    if project_stats.get("languages"):
        languages = "<br>".join(
            f"<b>{lang}</b>: {count} files"
            for lang, count in sorted(project_stats["languages"].items(), key=lambda x: -x[1])
        )

    errors_html = ""
    if result.errors:
        rows = "".join(f"<div class='err'>{escape(e)}</div>" for e in result.errors)
        errors_html = (
            f'<div class="card" style="margin-bottom:24px;border-color:#d93025">'
            f'<h3 style="color:#f85149">Errors During Analysis ({len(result.errors)})</h3>'
            f'{rows}'
            f'</div>'
        )

    grade_color = "#188038" if grade in ("A", "B") else "#e8710a" if grade == "C" else "#d93025"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Security Review — {escape(project_name)}</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background:#0d1117; color:#c9d1d9; padding: 32px; }}
  .page {{ max-width: 980px; margin: 0 auto; }}
  .header {{ border-bottom: 1px solid #21262d; padding-bottom: 20px; margin-bottom: 24px; }}
  h1 {{ font-size: 26px; color: #f0f6fc; }}
  .sub {{ color: #8b949e; margin-top: 6px; }}
  .grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 24px; }}
  .card {{ background:#161b22; border: 1px solid #21262d; border-radius: 8px; padding: 18px; }}
  .card h3 {{ color:#f0f6fc; font-size: 13px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px; }}
  .score {{ font-size: 52px; font-weight: 700; color: {grade_color}; }}
  .grade {{ font-size: 22px; color: {grade_color}; font-weight: 600; display:block; margin-top: 4px; }}
  .sev-row {{ display: flex; align-items: center; gap: 10px; margin-bottom: 8px; }}
  .sev-dot {{ width: 10px; height: 10px; border-radius: 50%; display:inline-block; flex: 0 0 10px; }}
  .sev-label {{ width: 90px; color: #c9d1d9; }}
  .sev-bar {{ flex: 1; background:#21262d; border-radius: 4px; height: 10px; overflow:hidden; }}
  .sev-fill {{ height: 100%; border-radius: 4px; }}
  .sev-count {{ width: 30px; text-align:right; color:#8b949e; }}
  .metrics {{ display: flex; gap: 28px; flex-wrap: wrap; color:#8b949e; font-size: 13px; margin-bottom: 8px; }}
  .finding {{ background:#161b22; border: 1px solid #21262d; border-left: 4px solid #30363d; border-radius: 8px; padding: 16px 18px; margin-bottom: 14px; }}
  .finding-head {{ display:flex; align-items:center; gap:10px; flex-wrap:wrap; }}
  .badge {{ color:#fff; font-size: 11px; font-weight:700; padding: 3px 9px; border-radius: 20px; text-transform: uppercase; letter-spacing: .5px; }}
  .finding-title {{ font-size: 15px; font-weight:600; color:#f0f6fc; }}
  .conf {{ margin-left:auto; font-size: 11px; color:#8b949e; }}
  .finding-meta {{ margin-top:6px; font-size: 12px; color:#8b949e; }}
  code {{ background:#21262d; padding: 2px 6px; border-radius: 4px; font-size: 12px; font-family: Consolas, monospace; }}
  .analyzer {{ background:#1f6feb22; color:#58a6ff; padding: 2px 8px; border-radius: 4px; margin-left: 8px; }}
  .finding-desc {{ margin-top: 10px; font-size: 13.5px; color:#c9d1d9; }}
  .finding-fix {{ margin-top: 6px; font-size: 13px; color:#8b949e; }}
  .code {{ background:#0d1117; border:1px solid #21262d; border-radius: 6px; padding: 12px; margin-top: 10px; font-family: Consolas, monospace; font-size: 12px; overflow-x:auto; color:#a5d6ff; }}
  .err {{ background:#d9302511; border:1px solid #d9302555; border-radius:6px; padding:10px 12px; margin:6px 0; font-family:Consolas,monospace; font-size:12px; color:#f85149; white-space:pre-wrap; }}
  details summary {{ cursor:pointer; color:#58a6ff; font-size:12px; margin-top:8px; }}
  .footer {{ color:#484f58; font-size: 11px; margin-top: 28px; text-align:center; }}
</style>
</head>
<body>
<div class="page">
  <div class="header">
    <h1>Security Review — {escape(project_name)}</h1>
    <div class="sub">Generated {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} &nbsp;·&nbsp; Analyzers: {escape(', '.join(analyzers_used))}</div>
    {f'<div class="sub">Path: <code>{escape(project_path)}</code></div>' if project_path else ''}
  </div>

  <div class="grid">
    <div class="card">
      <h3>Security Score</h3>
      <span class="score">{score:.0f}</span><span class="grade">Grade {grade}</span>
      <div class="metrics" style="margin-top:12px">
        <span>Bugs: {len(result.bugs)}</span>
        <span>Files: {result.files_analyzed}</span>
        <span>Lines: {project_stats.get('total_lines', 'N/A'):,}</span>
      </div>
    </div>
    <div class="card">
      <h3>Findings Breakdown</h3>
      {build_security_score_bars(result)}
    </div>
  </div>

  <div class="card" style="margin-bottom:24px">
    <h3>Scope</h3>
    {languages if languages else 'n/a'}
  </div>

  {errors_html}

  <h2 style="font-size:20px;color:#f0f6fc;margin-bottom:16px">Findings ({len(sorted_bugs)})</h2>
  {''.join(findings_html) if findings_html else '<div class="card">No issues were detected.</div>'}

  <div class="footer">Generated by BugHunter · AI-assisted automated security review · For auditing purposes only</div>
</div>
</body>
</html>
"""
    out_file.write_text(html, encoding="utf-8")
    return out_file