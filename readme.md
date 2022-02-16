# Format iPython Cells

[![Tests](https://github.com/janosh/format-ipy-cells/actions/workflows/test.yml/badge.svg)](https://github.com/janosh/format-ipy-cells/actions/workflows/test.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/janosh/format-ipy-cells/main.svg)](https://results.pre-commit.ci/latest/github/janosh/format-ipy-cells/main)
[![Requires Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org/downloads)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

Python code formatter (and [`pre-commit`](https://pre-commit.com) hook) for cell delimiters (`# %%`) in [VS Code-style interactive Python notebooks](https://code.visualstudio.com/docs/python/jupyter-support-py).

This formatter ensures

- cells are preceded by two empty lines:

    ```py
    # %%
    foo='bar'
    # %%
    ```

    ```py
    # %%
    foo='bar'


    # %%
    ```

- empty cells are removed:

    ```py
    # %%

    # %%
    ```

    ```py
    # %%
    ```

- same-line comments are separated by a single space:

    ```py
    # %%some comment
    foo = 'bar'
    # %%    another comment
    ```

    ```py
    # %% some comment
    foo = 'bar'
    # %% another comment
    ```

## Usage

### CLI

```sh
format-ipy-cells path/to/file.py
# or
format-ipy-cells **/*.py
```

## As `pre-commit` hook

Add this to your `.pre-commit-config.yaml`:

```yml
repos
  - repo: https://github.com/janosh/format-ipy-cells
    rev: v0.1.7
    hooks:
      - id: format-ipy-cells
```
