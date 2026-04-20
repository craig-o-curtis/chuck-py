# Agent Guidance

Trivial single-file Python project that fetches Chuck Norris jokes from api.chucknorris.io.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install ruff pytest mypy
```

## Developer Commands

| Command | Description |
|---------|-------------|
| `ruff check .` | Lint code |
| `mypy .` | Type check |
| `pytest` | Run tests |

## Project Structure

```
chuck.py      # Main script
tests/        # Test suite (pytest)
pyproject.toml  # Project config (ruff + mypy + pytest settings)
```

## Standard Order

`ruff check .` → `mypy .` → `pytest`