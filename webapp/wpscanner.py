"""Black-box WordPress security scanner.

Given a site URL, passively detects WordPress version, plugins, themes from
public pages (readme.html, asset paths, meta generator), checks them against
the WPVulnerability database (free, no API key), and runs safe config checks
(xmlrpc, wp-json user enumeration, debug mode, directory listing).

All checks are GET-only and non-intrusive.
"""
from __future__ import annotations

import json
import re
import urllib.parse
import urllib.request
from dataclasses import dataclass, field

UA = {"User-Agent": "BugHunter-WPScanner/1.0"}
TIMEOUT = 15
VULN_API = "https://www.wpvulnerability.net"


@dataclass
class Vuln:
    software: str
    software_type: str  # core|plugin|theme
    title: str
    max_affected: str
    cve: str
    severity: str = "high"


@dataclass
class Finding:
    check: str
    severity: str  # critical|high|medium|low|info
    title: str
    detail: str
    fix: str


@dataclass
class ScanResult:
    url: str
    is_wordpress: bool = False
    wp_version: str | None = None
    plugins: dict = field(default_factory=dict)   # slug -> version|None
    theme: str | None = None
    vulns: list = field(default_factory=list)
    findings: list = field(default_factory=list)
    errors: list = field(default_factory=list)


def _get(url: str, timeout: int = TIMEOUT) -> tuple[int, str, dict]:
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read(2_000_000).decode("utf-8", errors="replace")
            return resp.status, body, dict(resp.headers)
    except urllib.error.HTTPError as e:
        try:
            body = e.read(500_000).decode("utf-8", errors="replace")
        except Exception:
            body = ""
        return e.code, body, {}
    except Exception:
        return 0, "", {}


def _api_get(path: str):
    status, body, _ = _get(VULN_API + path)
    if status != 200 or not body:
        return None
    try:
        return json.loads(body)
    except json.JSONDecodeError:
        return None


def detect_wordpress(base: str) -> ScanResult:
    res = ScanResult(url=base)
    base = base.rstrip("/")

    status, html, headers = _get(base + "/")
    if status == 0:
        res.errors.append("Site is unreachable")
        return res

    # WP signals: meta generator, wp-content paths, wp-json link
    gen = re.search(r'<meta\s+name=["\']generator["\']\s+content=["\']WordPress\s*([\d.]*)', html, re.I)
    has_wp_content = "wp-content/" in html or "wp-includes/" in html
    if gen:
        res.is_wordpress = True
        res.wp_version = gen.group(1) or None
    elif has_wp_content:
        res.is_wordpress = True

    if not res.is_wordpress:
        # Try readme.html — classic WP fingerprint
        st, readme, _ = _get(base + "/readme.html")
        if st == 200 and "WordPress" in readme:
            res.is_wordpress = True
            m = re.search(r"Version\s+([\d.]+)", readme)
            if m:
                res.wp_version = m.group(1)
        else:
            return res

    # WP version fallback: feed or login page CSS version
    if not res.wp_version:
        st, login, _ = _get(base + "/wp-login.php")
        if st == 200:
            m = re.search(r"ver=([\d.]+)", login)
            if m:
                res.wp_version = m.group(1)

    # Plugins & theme from asset paths: /wp-content/plugins/<slug>/, /themes/<slug>/
    for m in re.finditer(r"/wp-content/plugins/([a-z0-9\-_]+)/", html, re.I):
        res.plugins.setdefault(m.group(1).lower(), None)
    for m in re.finditer(r"/wp-content/themes/([a-z0-9\-_]+)/", html, re.I):
        if not res.theme:
            res.theme = m.group(1).lower()

    # Plugin versions via readme.txt for detected plugins (up to 15)
    for slug in list(res.plugins)[:15]:
        st, txt, _ = _get(f"{base}/wp-content/plugins/{slug}/readme.txt")
        if st == 200:
            m = re.search(r"Stable tag:\s*([\d.]+)", txt)
            if m:
                res.plugins[slug] = m.group(1)

    return res


def check_vulns(res: ScanResult):
    targets = []
    if res.wp_version:
        targets.append(("core", "wordpress", res.wp_version))
    for slug, ver in res.plugins.items():
        targets.append(("plugin", slug, ver))
    if res.theme:
        targets.append(("theme", res.theme, None))

    for sw_type, slug, ver in targets:
        data = _api_get(f"/{sw_type}/{slug}")
        if not data or data.get("error"):
            continue
        for v in (data.get("data", {}) or {}).get("vulnerability", []) or []:
            op = v.get("operator", {})
            max_v = op.get("max_version")
            # Version filter: report when installed version is below the fixed one
            if ver and max_v and _version_gte(ver, max_v):
                continue
            cve = ""
            for s in v.get("source", []) or []:
                if str(s.get("id", "")).startswith("CVE"):
                    cve = s["id"]
                    break
            res.vulns.append(Vuln(
                software=slug,
                software_type=sw_type,
                title=v.get("name", "Known vulnerability"),
                max_affected=max_v or "?",
                cve=cve,
                severity="high" if sw_type == "core" else "medium",
            ))


def check_config(res: ScanResult):
    base = res.url.rstrip("/")

    # 1. xmlrpc.php exposed (pingback DDoS / brute force amplification)
    st, body, _ = _get(base + "/xmlrpc.php")
    if st == 200 and "XML-RPC server accepts POST requests only" in body:
        res.findings.append(Finding(
            "xmlrpc", "medium", "XML-RPC enabled",
            "xmlrpc.php is publicly accessible — enables brute-force amplification and pingback abuse.",
            "Disable XML-RPC (plugin or .htaccess deny) if not needed.",
        ))

    # 2. User enumeration via REST API
    st, body, _ = _get(base + "/wp-json/wp/v2/users")
    if st == 200 and body.strip().startswith("["):
        try:
            users = json.loads(body)
            if users and isinstance(users, list):
                names = ", ".join(str(u.get("slug", "?")) for u in users[:5])
                res.findings.append(Finding(
                    "user-enum", "medium", "User enumeration via REST API",
                    f"/wp-json/wp/v2/users exposes usernames: {names}. Aids brute-force attacks.",
                    "Restrict /users endpoint (security plugin or REST filter).",
                ))
        except json.JSONDecodeError:
            pass

    # 3. Debug mode (display errors / wp-config backup)
    st, body, _ = _get(base + "/wp-config.php.swp")
    if st == 200 and len(body) > 50:
        res.findings.append(Finding(
            "config-backup", "critical", "wp-config backup file exposed",
            "wp-config.php.swp is downloadable — likely contains DB credentials.",
            "Delete backup copies of wp-config.php immediately.",
        ))

    # 4. Directory listing on uploads
    st, body, _ = _get(base + "/wp-content/uploads/")
    if st == 200 and ("Index of" in body or "Parent Directory" in body):
        res.findings.append(Finding(
            "dir-listing", "low", "Directory listing on uploads",
            "/wp-content/uploads/ shows a file index — leaks file names and structure.",
            "Disable directory indexing (Options -Indexes).",
        ))

    # 5. Outdated core
    if res.wp_version and _version_lt(res.wp_version, "6.0"):
        res.findings.append(Finding(
            "outdated-core", "high", f"Outdated WordPress core {res.wp_version}",
            f"Site runs WordPress {res.wp_version} — far behind current releases, unpatched CVEs likely.",
            "Update WordPress core to the latest version.",
        ))


def _version_gte(a: str, b: str) -> bool:
    def parts(v):
        return [int(x) if x.isdigit() else 0 for x in re.split(r"[.-]", v)[:4]]
    pa, pb = parts(a), parts(b)
    pa += [0] * (len(pb) - len(pa))
    pb += [0] * (len(pa) - len(pb))
    return pa >= pb


def _version_lt(a: str, b: str) -> bool:
    return not _version_gte(a, b)


def scan_wordpress(url: str) -> ScanResult:
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    res = detect_wordpress(url)
    if not res.is_wordpress:
        res.errors.append("Does not look like a WordPress site")
        return res
    check_vulns(res)
    check_config(res)
    return res
