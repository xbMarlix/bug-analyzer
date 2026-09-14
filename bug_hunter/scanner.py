from pathlib import Path

from config import (
    EXTENSION_LANGUAGE_MAP,
    IGNORED_DIRS,
    IGNORED_FILES,
    MAX_FILE_SIZE_KB,
)


class ScannedFile:
    def __init__(self, path: Path, language: str, content: str):
        self.path = path
        self.language = language
        self.content = content
        self.relative_path = None

    def __repr__(self):
        return f"ScannedFile({self.relative_path}, {self.language})"


def detect_language(file_path: Path) -> str | None:
    return EXTENSION_LANGUAGE_MAP.get(file_path.suffix.lower())


def should_ignore(path: Path) -> bool:
    for part in path.parts:
        if part in IGNORED_DIRS:
            return True
    if path.name in IGNORED_FILES:
        return True
    return False


def scan_project(project_path: str | Path) -> list[ScannedFile]:
    project = Path(project_path).resolve()
    if not project.is_dir():
        raise FileNotFoundError(f"Project not found: {project}")

    files = []
    for file_path in project.rglob("*"):
        if not file_path.is_file():
            continue
        if should_ignore(file_path.relative_to(project)):
            continue

        language = detect_language(file_path)
        if language is None:
            continue

        size_kb = file_path.stat().st_size / 1024
        if size_kb > MAX_FILE_SIZE_KB:
            continue

        try:
            raw = file_path.read_bytes()
        except (OSError, PermissionError):
            continue

        try:
            content = raw.decode("utf-8")
        except UnicodeDecodeError:
            # Binary or non-UTF-8 file: skip explicitly instead of silently
            # corrupting bytes with errors="ignore".
            continue

        scanned = ScannedFile(file_path, language, content)
        scanned.relative_path = file_path.relative_to(project)
        files.append(scanned)

    return files


def get_project_stats(files: list[ScannedFile]) -> dict:
    languages = {}
    for f in files:
        languages[f.language] = languages.get(f.language, 0) + 1
    total_lines = sum(f.content.count("\n") + 1 for f in files)
    return {
        "total_files": len(files),
        "total_lines": total_lines,
        "languages": languages,
    }
