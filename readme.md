# Format iPython Cells

[![Tests](https://github.com/janosh/format-ipy-cells/workflows/Tests/badge.svg)](https://github.com/janosh/format-ipy-cells/actions)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/janosh/format-ipy-cells/main.svg)](https://results.pre-commit.ci/latest/github/janosh/format-ipy-cells/main)
[![Requires Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org/downloads)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

[`pre-commit`](https://pre-commit.com) hook and Python code formatter for cell delimiters (`# %%`) in interactive Python notebooks. Ensures

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

## Usage as CLI

```sh
format-ipy-cells path/to/file.py
```

To run on all Python files in a project, use wildcards:

```sh
format-ipy-cells **/*.py
```

To get the current version, use `-v/--version`.

```sh
format-ipy-cells -v
>>> Format iPython Cells v0.1.6
```

## Install as `pre-commit` hook

Add this to your `.pre-commit-config.yaml`:

```yml
repos
  - repo: https://github.com/janosh/format-ipy-cells
    rev: v0.1.6
    hooks:
      - id: format-ipy-cells
```
