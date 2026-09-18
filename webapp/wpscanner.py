"""Black-box website security scanner (any site, WordPress included).

Passive, GET-only checks:
- Tech fingerprinting (WordPress, Joomla, Drupal, frameworks, servers)
- Security headers (CSP, HSTS, X-Frame-Options, etc.)
- Exposed sensitive files (.git, .env, backups, config)
- Secrets leaked in public JS
- WordPress-specific: version/plugins/themes + WPVulnDB + config checks

Non-intrusive by design: a handful of GET requests, no fuzzing, no POST.
"""
from __future__ import annotations

import json
import re
import urllib.request
from dataclasses import dataclass, field

UA = {"User-Agent": "BugHunter-SiteScanner/1.0"}
TIMEOUT = 15
VULN_API = "https://www.wpvulnerability.net"


@dataclass
class Vuln:
    software: str
    software_type: str
    title: str
    max_affected: str
    cve: str
    severity: str = "high"


@dataclass
class Finding:
    check: str
    severity: str
    title: str
    detail: str
    fix: str


@dataclass
class ScanResult:
    url: str
    is_wordpress: bool = False
    wp_version: str | None = None
    plugins: dict = field(default_factory=dict)
    theme: str | None = None
    technologies: list = field(default_factory=list)
    server: str | None = None
    missing_headers: list = field(default_factory=list)
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


_SECURITY_HEADERS = {
    "content-security-policy": ("medium", "No Content-Security-Policy",
                                 "CSP header is missing — XSS attacks are easier to execute.",
                                 "Add a Content-Security-Policy header."),
    "strict-transport-security": ("medium", "No HSTS",
                                   "Strict-Transport-Security missing — connections can be downgraded to HTTP.",
                                   "Enable HSTS (max-age >= 31536000)."),
    "x-frame-options": ("low", "No X-Frame-Options",
                        "Page can be embedded in an iframe — clickjacking possible.",
                        "Set X-Frame-Options: DENY or SAMEORIGIN (or CSP frame-ancestors)."),
    "x-content-type-options": ("low", "No X-Content-Type-Options",
                               "MIME sniffing allowed — browsers may misinterpret files as scripts.",
                               "Set X-Content-Type-Options: nosniff."),
    "referrer-policy": ("info", "No Referrer-Policy",
                        "Referrer may leak internal URLs to third parties.",
                        "Set Referrer-Policy: strict-origin-when-cross-origin."),
    "permissions-policy": ("info", "No Permissions-Policy",
                           "Browser features (camera, mic, geo) not restricted.",
                           "Set a Permissions-Policy header."),
}


def check_headers(res: ScanResult, headers: dict):
    lower = {k.lower(): v for k, v in headers.items()}
    res.server = lower.get("server") or lower.get("x-powered-by")
    if res.server:
        res.technologies.append(f"Server: {res.server}")
    for h, (sev, title, detail, fix) in _SECURITY_HEADERS.items():
        if h not in lower:
            res.missing_headers.append(h)
            res.findings.append(Finding(f"header-{h}", sev, title, detail, fix))


def fingerprint(res: ScanResult, html: str, headers: dict):
    techs = set()
    lower_headers = {k.lower(): v for k, v in headers.items()}

    if "wp-content/" in html or "wp-includes/" in html or re.search(
            r'<meta\s+name=["\']generator["\']\s+content=["\']WordPress', html, re.I):
        techs.add("WordPress")
    if re.search(r'<meta\s+name=["\']generator["\']\s+content=["\']Joomla', html, re.I) or "/media/joomla/" in html:
        techs.add("Joomla")
    if re.search(r"Drupal\.settings", html) or "/sites/default/files/" in html:
        techs.add("Drupal")
    if "__NEXT_DATA__" in html or "/_next/static/" in html:
        techs.add("Next.js")
    if "react-root" in html or "data-reactroot" in html or re.search(r"react(?:\.production)?(?:\.min)?\.js", html, re.I):
        techs.add("React")
    if re.search(r"vue(?:\.runtime)?(?:\.min)?\.js|data-v-[0-9a-f]{8}", html, re.I) or "__vue__" in html:
        techs.add("Vue.js")
    if "ng-version" in html or re.search(r"angular(?:\.min)?\.js", html, re.I):
        techs.add("Angular")
    if re.search(r"jquery[-.]?(?:\d+\.\d+\.\d+)?(?:\.min)?\.js", html, re.I):
        techs.add("jQuery")
    if "bootstrap" in html.lower():
        techs.add("Bootstrap")
    if lower_headers.get("x-powered-by"):
        techs.add(f"Powered by {lower_headers['x-powered-by']}")
    if lower_headers.get("x-generator"):
        techs.add(f"Generator: {lower_headers['x-generator']}")

    res.technologies = sorted(set(res.technologies) | techs)


def check_exposed_files(res: ScanResult, base: str):
    probes = [
        ("/.git/HEAD", "critical", "Git repository exposed",
         ".git/HEAD is publicly accessible — the entire source code history can be downloaded.",
         "Block .git in the web server config and remove it from the web root."),
        ("/.env", "critical", ".env file exposed",
         "Environment file is publicly accessible — usually contains DB passwords and API keys.",
         "Remove .env from the web root; rotate all secrets in it NOW."),
        ("/.git/config", "high", "Git config exposed",
         ".git/config reveals repository remotes and structure.",
         "Block .git access in the web server."),
        ("/backup.sql", "high", "Possible SQL backup exposed",
         "A backup.sql file responded publicly — may contain the full database.",
         "Remove database dumps from the web root."),
        ("/config.php.bak", "high", "Config backup exposed",
         "A backup copy of config is publicly accessible — likely contains credentials.",
         "Delete *.bak copies from the web root."),
        ("/phpinfo.php", "medium", "phpinfo() page exposed",
         "phpinfo.php reveals server configuration, paths, and modules.",
         "Remove phpinfo() scripts from production."),
        ("/server-status", "medium", "Server status page exposed",
         "Apache server-status leaks requests, IPs, and uptime.",
         "Restrict server-status to localhost."),
        ("/.DS_Store", "low", ".DS_Store exposed",
         "macOS .DS_Store leaks directory file listings.",
         "Delete .DS_Store and block it in the web server."),
    ]
    for path, sev, title, detail, fix in probes:
        st, body, _ = _get(base + path, timeout=8)
        if st == 200 and len(body) > 20:
            if path == "/.git/HEAD" and "ref:" not in body:
                continue
            if path == "/.env" and not re.search(r"(DB_|KEY|SECRET|PASSWORD|TOKEN)=", body):
                continue
            res.findings.append(Finding(f"exposed{path}", sev, title, detail, fix))


def check_js_secrets(res: ScanResult, base: str, html: str):
    scripts = re.findall(r'<script[^>]+src=["\']([^"\']+\.js[^"\']*)', html, re.I)[:10]
    secret_re = re.compile(
        r"(?:api[_-]?key|apikey|secret|token|password)['\"\s:=]{1,10}['\"]([A-Za-z0-9_\-]{20,})['\"]",
        re.I,
    )
    placeholder = re.compile(r"^(token|secret|password|apikey|api_key|example|test|demo|xxx|placeholder|none)", re.I)
    for src in scripts:
        full = src if src.startswith("http") else base + ("" if src.startswith("/") else "/") + src
        st, body, _ = _get(full, timeout=8)
        if st != 200:
            continue
        for m in secret_re.finditer(body):
            value = m.group(1)
            if placeholder.match(value) or (value.isalpha() and value.islower()):
                continue
            res.findings.append(Finding(
                "js-secret", "high", "Possible hardcoded secret in JavaScript",
                f"{src}: a 20+ char token-like value is embedded in public JS: {value[:6]}…{value[-4:]}",
                "Move secrets server-side; rotate this key — it is public.",
            ))
            break


def detect_wordpress(res: ScanResult, base: str, html: str):
    gen = re.search(r'<meta\s+name=["\']generator["\']\s+content=["\']WordPress\s*([\d.]*)', html, re.I)
    has_wp_content = "wp-content/" in html or "wp-includes/" in html
    if gen:
        res.is_wordpress = True
        res.wp_version = gen.group(1) or None
    elif has_wp_content:
        res.is_wordpress = True

    if not res.is_wordpress:
        st, readme, _ = _get(base + "/readme.html")
        if st == 200 and "WordPress" in readme:
            res.is_wordpress = True
            m = re.search(r"Version\s+([\d.]+)", readme)
            if m:
                res.wp_version = m.group(1)

    if not res.is_wordpress:
        return

    if not res.wp_version:
        st, login, _ = _get(base + "/wp-login.php")
        if st == 200:
            m = re.search(r"ver=([\d.]+)", login)
            if m:
                res.wp_version = m.group(1)

    for m in re.finditer(r"/wp-content/plugins/([a-z0-9\-_]+)/", html, re.I):
        res.plugins.setdefault(m.group(1).lower(), None)
    for m in re.finditer(r"/wp-content/themes/([a-z0-9\-_]+)/", html, re.I):
        if not res.theme:
            res.theme = m.group(1).lower()

    for slug in list(res.plugins)[:15]:
        st, txt, _ = _get(f"{base}/wp-content/plugins/{slug}/readme.txt")
        if st == 200:
            m = re.search(r"Stable tag:\s*([\d.]+)", txt)
            if m:
                res.plugins[slug] = m.group(1)


def check_wp_vulns(res: ScanResult):
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
            if ver and max_v and _version_gte(ver, max_v):
                continue
            cve = ""
            for s in v.get("source", []) or []:
                if str(s.get("id", "")).startswith("CVE"):
                    cve = s["id"]
                    break
            res.vulns.append(Vuln(
                software=slug, software_type=sw_type,
                title=v.get("name", "Known vulnerability"),
                max_affected=max_v or "?", cve=cve,
                severity="high" if sw_type == "core" else "medium",
            ))


def check_wp_config(res: ScanResult, base: str):
    st, body, _ = _get(base + "/xmlrpc.php")
    if st == 200 and "XML-RPC server accepts POST requests only" in body:
        res.findings.append(Finding(
            "xmlrpc", "medium", "XML-RPC enabled",
            "xmlrpc.php is publicly accessible — enables brute-force amplification and pingback abuse.",
            "Disable XML-RPC (plugin or .htaccess deny) if not needed.",
        ))

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

    st, body, _ = _get(base + "/wp-config.php.swp")
    if st == 200 and len(body) > 50:
        res.findings.append(Finding(
            "config-backup", "critical", "wp-config backup file exposed",
            "wp-config.php.swp is downloadable — likely contains DB credentials.",
            "Delete backup copies of wp-config.php immediately.",
        ))

    st, body, _ = _get(base + "/wp-content/uploads/")
    if st == 200 and ("Index of" in body or "Parent Directory" in body):
        res.findings.append(Finding(
            "dir-listing", "low", "Directory listing on uploads",
            "/wp-content/uploads/ shows a file index — leaks file names and structure.",
            "Disable directory indexing (Options -Indexes).",
        ))

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


def scan_website(url: str) -> ScanResult:
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    base = url.rstrip("/")
    res = ScanResult(url=base)

    status, html, headers = _get(base + "/")
    if status == 0:
        res.errors.append("Site is unreachable")
        return res

    fingerprint(res, html, headers)
    check_headers(res, headers)
    check_exposed_files(res, base)
    check_js_secrets(res, base, html)

    detect_wordpress(res, base, html)
    if res.is_wordpress:
        check_wp_vulns(res)
        check_wp_config(res, base)

    return res


def scan_wordpress(url: str) -> ScanResult:
    return scan_website(url)
