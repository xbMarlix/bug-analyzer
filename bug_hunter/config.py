import os
from pathlib import Path

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
OPENAI_MODEL = os.environ.get("OPENAI_MODEL", "gpt-4o")
OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL", "")

MAX_FILE_SIZE_KB = 500
MAX_AI_CHUNK_LINES = 500
# Lines of overlap between consecutive AI chunks so a state-write / call pair
# spanning a chunk boundary is still seen together by the model. Larger overlap
# reduces missed findings at the cost of more tokens per file.
AI_CHUNK_OVERLAP = 24
# Base delay (seconds) and cap for exponential backoff on 429/transient API errors.
AI_BACKOFF_BASE_S = 2.0
AI_BACKOFF_MAX_RETRIES = 4

# Directories that are skipped entirely (by name, at any depth). Note: this
# intentionally excludes `test`/`tests`/`lib`/`script`/`scripts`/`docs`/`audit`
# and dependency/build/vendored trees, so unit-test suites, deployment scripts
# and third-party libraries are NOT scanned by any analyzer. If you want the
# tool to audit a test harness or an embedded library, remove the matching
# entry (or scan that directory directly by pointing the scanner at it).
IGNORED_DIRS = {
    ".git", "node_modules", "__pycache__", ".venv", "venv",
    "env", ".env", "dist", "build", ".next", ".nuxt",
    "vendor", "target", ".idea", ".vscode", "egg-info",
    "lib", "test", "tests", "script", "scripts", "docs", "audit",
    "out", "cache", "broadcast", "mocks",
    "archive", "archived", "deprecated", "old", "legacy",
}

IGNORED_FILES = {
    "package-lock.json", "yarn.lock", "poetry.lock",
    "Pipfile.lock", "go.sum", "Cargo.lock", "foundry.toml",
}

EXTENSION_LANGUAGE_MAP = {
    ".py": "python",
    ".js": "javascript",
    ".jsx": "javascript",
    ".ts": "typescript",
    ".tsx": "typescript",
    ".go": "go",
    ".java": "java",
    ".rs": "rust",
    ".rb": "ruby",
    ".php": "php",
    ".c": "c",
    ".cpp": "cpp",
    ".h": "c",
    ".hpp": "cpp",
    ".cs": "csharp",
    ".swift": "swift",
    ".kt": "kotlin",
    ".scala": "scala",
    ".sh": "bash",
    ".bash": "bash",
    ".sql": "sql",
    ".html": "html",
    ".css": "css",
    ".scss": "scss",
    ".sol": "solidity",
    ".vy": "vyper",
}

REPORT_DIR = Path("bug_hunter_reports")

SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4}
