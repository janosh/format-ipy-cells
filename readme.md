# Format iPython Cells

[![Tests](https://github.com/janosh/format-ipy-cells/workflows/Tests/badge.svg)](https://github.com/janosh/format-ipy-cells/actions)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/janosh/format-ipy-cells/main.svg)](https://results.pre-commit.ci/latest/github/janosh/format-ipy-cells/main)
[![This project supports Python 3.6+](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://python.org/downloads)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

[`pre-commit`](https://pre-commit.com) hook and Python code formatter that ensures iPython cell delimiters (`# %%`) are preceded by two empty lines and separated from comments by a single space.

## Usage as CLI

`format-ipy-cells` has the following flags:

- `--filenames` (required): File paths to format.

## Install as `pre-commit` hook

Add this to your `.pre-commit-config.yaml`:

```yml
repos
  - repo: https://github.com/janosh/format-ipy-cells
    rev: v0.1.1
    hooks:
      - id: format-ipy-cells
```
