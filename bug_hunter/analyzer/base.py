from dataclasses import dataclass, field


@dataclass
class Bug:
    file: str
    line: int
    column: int
    severity: str
    category: str
    title: str
    description: str
    suggestion: str
    code_snippet: str = ""
    analyzer: str = ""
    confidence: float = 1.0


@dataclass
class AnalysisResult:
    bugs: list[Bug] = field(default_factory=list)
    files_analyzed: int = 0
    errors: list[str] = field(default_factory=list)

    def add(self, bug: Bug):
        self.bugs.append(bug)

    def merge(self, other: "AnalysisResult"):
        self.bugs.extend(other.bugs)
        self.files_analyzed = max(self.files_analyzed, other.files_analyzed)
        self.errors.extend(other.errors)

    def sorted_bugs(self, by: str = "severity") -> list[Bug]:
        from config import SEVERITY_ORDER
        return sorted(self.bugs, key=lambda b: SEVERITY_ORDER.get(b.severity, 99))


class BaseAnalyzer:
    name = "base"

    def analyze(self, files: list) -> AnalysisResult:
        raise NotImplementedError
