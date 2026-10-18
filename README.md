# risk-lab

[![CI](https://github.com/hilton-eng/risk-lab/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/hilton-eng/risk-lab/actions/workflows/ci.yml)

A small Python package used to practise professional engineering habits: reproducible environments with uv, tests, linting, type checking, pre-commit hooks and CI.

## Setup

```bash
uv sync
uv run pre-commit install
```

## Checks

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy src
uv run pytest -v
```

The same checks run in GitHub Actions on every pull request.
