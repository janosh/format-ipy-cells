"""format_ipy_cells helper functions tests."""

import pytest

from format_ipy_cells import helpers


@pytest.mark.parametrize("raw_delim", ["#    %%", "#%%"])
def test_format_cell_delimiters(raw_delim: str) -> None:
    assert helpers.format_cell_delimiters(raw_delim) == "# %%"


@pytest.mark.parametrize("line", ["# %%some comment", "# %%     some comment"])
def test_format_comments_after_cell_delimiters(line: str) -> None:
    assert helpers.format_comments_after_cell_delimiters(line) == "# %% some comment"


def test_remove_empty_cells() -> None:
    # single empty cell
    out = helpers.remove_empty_cells("# %%\n\n# %%")
    assert out == "# %%"

    # single empty cell with comment
    out = helpers.remove_empty_cells("# %% comment\n\n# %%")
    assert out == "# %% comment"

    # two empty cells with comment
    out = helpers.remove_empty_cells("# %% comment\n\n# %%\n\n# %%")
    assert out == "# %% comment"

    # two empty cells with comment and spaces
    out = helpers.remove_empty_cells("# %% comment\n  \n   # %%\n  \n  # %%")
    assert out == "# %% comment"


@pytest.mark.parametrize(
    "line",
    [
        # cell with single blank line between delimiter and first code line
        "# %%\n\nfoo = 'bar'",
        # cell with 4 blank lines between cell delimiter and first code line
        "# %%\n\n\n\nfoo = 'bar'",
        # cell with 4 blank and spaces lines between cell delimiter and first code line
        "# %%\n\t\t\n  \n    \nfoo = 'bar'",
    ],
)
def test_remove_empty_lines_starting_cell(line: str) -> None:
    assert helpers.remove_empty_lines_starting_cell(line) == "# %%\nfoo = 'bar'"


def test_ensure_two_blank_lines_preceding_cell() -> None:
    # single preceding blank line
    out = helpers.ensure_two_blank_lines_preceding_cell("\n# %%\n")
    assert out == "\n\n\n# %%\n"

    # single preceding blank line with code in cell
    out = helpers.ensure_two_blank_lines_preceding_cell("\n# %%\nfoo = 'bar'")
    assert out == "\n\n\n# %%\nfoo = 'bar'"

    # too many preceding blank line with code in cell
    out = helpers.ensure_two_blank_lines_preceding_cell("\n\n\n\n\n\n# %%\nfoo = 'bar'")
    assert out == "\n\n\n# %%\nfoo = 'bar'"


@pytest.mark.parametrize(
    "line",
    [
        # empty last cell containing single blank line
        "\n# %%\na = 5\n\n\n# %%\n",
        # empty last cell containing many blank lines
        "\n# %%\na = 5\n\n\n# %%\n\n\n\n",
        # empty last cell containing many blank lines + other white space
        "\n# %%\na = 5\n\n\n# %%\n\t  \n\n   \n",
    ],
)
def test_delete_last_cell_if_empty(line: str) -> None:
    assert helpers.delete_last_cell_if_empty(line) == "\n# %%\na = 5\n"
