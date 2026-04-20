# Chuck Joke

Simple Python script that fetches Chuck Norris jokes from api.chucknorris.io.

## Setup

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate  # Windows

# Install dependencies
pip install ruff pytest mypy
```

## Development

```bash
# Lint
ruff check .

# Type check
mypy .

# Run tests
pytest
```

## Run

```bash
python3 chuck.py
```