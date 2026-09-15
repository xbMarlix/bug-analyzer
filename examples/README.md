# Example Reports — BugHunter in Action

Real scan results (static mode, no AI — the free tier) on well-known
intentionally-vulnerable training projects. These are industry-standard
benchmarks for security scanners.

| Project | Language | Critical | High | Medium | Report |
|---------|----------|---------|------|--------|--------|
| [DVWA](https://github.com/digininja/DVWA) | PHP/JS | 17 | 7 | 11 | [report_DVWA.md](report_DVWA.md) |
| [OWASP Juice Shop](https://github.com/juice-shop/juice-shop) | TypeScript/JS | 13 | 13 | 45 | [report_juice-shop.md](report_juice-shop.md) |
| [WebGoat](https://github.com/WebGoat/WebGoat) | Java | 47 | 176 | 57 | [report_WebGoat.md](report_WebGoat.md) |

Each scan takes under 2 seconds on these codebases (static mode).
AI mode (`--model gpt-4o` or a local LLM) adds deep semantic findings with
concrete exploit paths and verifies rule candidates to cut false positives.

To scan your own project:

```bash
pip install -e .
bug-hunter /path/to/your/project --static-only
```
