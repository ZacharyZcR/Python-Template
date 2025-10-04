# Python Template

A highly engineered Python project template with strict quality controls and automated CI/CD.

[![CI](https://github.com/yourusername/python-template/workflows/CI/badge.svg)](https://github.com/yourusername/python-template/actions)
[![codecov](https://codecov.io/gh/yourusername/python-template/branch/main/graph/badge.svg)](https://codecov.io/gh/yourusername/python-template)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

## Features

**Quality Control:**
- 🚀 **Ruff** - Lightning-fast linting and formatting (replaces Black, Flake8, isort)
- 🔍 **Mypy** - Static type checking
- 📊 **Pytest** - Testing framework with 80%+ coverage requirement
- 📝 **Interrogate** - Docstring coverage enforcement (80%+)
- 🔬 **Radon** - Code complexity analysis
- 🎯 **Pre-commit hooks** - Automatic quality checks before commit

**CI/CD:**
- ✅ GitHub Actions for automated testing across Python 3.9-3.12
- 🔄 Automated dependency updates via Dependabot
- 📦 Automated releases to PyPI
- 📈 Code coverage reporting to Codecov

**Developer Experience:**
- 📋 Makefile with common commands
- 🎨 Modern `pyproject.toml` configuration
- 📚 Example code with best practices
- 🔧 VS Code and PyCharm compatible

## Quick Start

### Use as Template

1. Click "Use this template" on GitHub
2. Clone your new repository
3. Update project metadata in `pyproject.toml`
4. Install dependencies:

```bash
make install-dev
```

### Project Structure

```
python-template/
├── src/                    # Source code
│   ├── core/              # Core functionality
│   └── utils/             # Utility functions
├── tests/                 # Tests
│   ├── unit/             # Unit tests
│   └── integration/      # Integration tests
├── .github/
│   └── workflows/        # CI/CD pipelines
├── pyproject.toml        # Project configuration
├── .pre-commit-config.yaml
├── Makefile              # Common commands
└── README.md
```

## Development

### Setup

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install with development dependencies
make install-dev
```

### Common Commands

```bash
make help              # Show all available commands
make test              # Run tests with coverage
make lint              # Check code quality
make format            # Auto-format code
make quality           # Run all quality checks
make clean             # Clean build artifacts
```

### Quality Standards

This template enforces strict quality standards:

| Check | Tool | Standard |
|-------|------|----------|
| Code Style | Ruff | PEP 8 compliant, 100 chars/line |
| Type Hints | Mypy | Required for all functions |
| Test Coverage | Pytest | ≥ 80% |
| Docstring Coverage | Interrogate | ≥ 80% |
| Complexity | Radon | Cyclomatic ≤ 10 (B grade) |

### Pre-commit Hooks

Hooks run automatically on `git commit`:

```bash
# Manual run on all files
make pre-commit

# Update hook versions
pre-commit autoupdate
```

### Writing Tests

```python
# tests/unit/test_example.py
import pytest
from src.core.calculator import Calculator

def test_addition() -> None:
    """Test that addition works correctly."""
    assert Calculator.add(2, 3) == 5
```

Run tests:
```bash
make test              # With coverage
make test-fast         # Without coverage
```

## CI/CD

### Continuous Integration

On every push and PR:
- ✅ Code quality checks (lint, format, type)
- ✅ Tests across Python 3.9-3.12
- ✅ Coverage reporting
- ✅ Build verification

### Releases

Automatic release on version tags:

```bash
# Create and push a tag
git tag v1.0.0
git push origin v1.0.0
```

This triggers:
1. Build distribution packages
2. Create GitHub release
3. Publish to PyPI (requires `PYPI_API_TOKEN` secret)

## Configuration

### pyproject.toml

All tools configured in one place:
- Project metadata
- Dependencies
- Ruff settings
- Mypy settings
- Pytest settings
- Coverage settings
- Interrogate settings

### Customization

Adjust quality thresholds in `pyproject.toml`:

```toml
# Example: Lower coverage requirement
[tool.pytest.ini_options]
addopts = ["--cov-fail-under=70"]

# Example: Adjust line length
[tool.ruff]
line-length = 120
```

## Tools Explained

### Why Ruff?

Ruff is 10-100x faster than traditional Python linters:
- **Replaces**: Black (formatting) + Flake8 (linting) + isort (imports)
- **Written in**: Rust (blazingly fast)
- **Benefit**: One tool, one config, instant feedback

### Why These Coverage Thresholds?

- **80% code coverage**: Catches most bugs without diminishing returns
- **80% docstring coverage**: Ensures public APIs are documented
- **Complexity ≤ 10**: Functions remain testable and maintainable

## Troubleshooting

### Pre-commit Hook Failures

```bash
# See what failed
git commit -m "message"

# Fix issues
make format        # Auto-fix formatting
make lint-fix      # Auto-fix linting

# Try again
git commit -m "message"
```

### Type Check Errors

```bash
# Run type check
make type-check

# Common fix: Add type hints
def my_function(x: int) -> str:
    return str(x)
```

### Test Failures

```bash
# Run specific test
pytest tests/unit/test_calculator.py::test_add

# See detailed output
pytest -vv

# Debug with print statements
pytest -s
```

## Contributing

1. Create feature branch: `git checkout -b feature-name`
2. Make changes and commit (hooks will run)
3. Push and create PR
4. CI must pass before merge

## License

This template is released under the MIT License. Use it freely!

---

**Built with quality in mind. Ship code with confidence.**
