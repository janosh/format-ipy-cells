# Format iPython Cells

[![Tests](https://github.com/janosh/format-ipy-cells/workflows/Tests/badge.svg)](https://github.com/janosh/format-ipy-cells/actions)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/janosh/format-ipy-cells/main.svg)](https://results.pre-commit.ci/latest/github/janosh/format-ipy-cells/main)
[![This project supports Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org/downloads)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

[`pre-commit`](https://pre-commit.com) hook and Python code formatter for iPython cell delimiters (`# %%`). Ensures

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
format-ipy-cells path/to/one-or-more/files
```

## Install as `pre-commit` hook

Add this to your `.pre-commit-config.yaml`:

```yml
repos
  - repo: https://github.com/janosh/format-ipy-cells
    rev: v0.1.4
    hooks:
      - id: format-ipy-cells
```
