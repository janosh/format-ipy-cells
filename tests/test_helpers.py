from format_ipy_cells.helpers import (
    delete_last_cell_if_empty,
    ensure_two_blank_lines_preceding_cell,
    format_cell_delimeters,
    format_comments_after_cell_delimeters,
    remove_empty_cells,
    remove_empty_lines_starting_cell,
)


def test_format_cell_delimeters():

    out = format_cell_delimeters("#    %%")
    assert out == "# %%"

    out = format_cell_delimeters("#%%")
    assert out == "# %%"


def test_format_comments_after_cell_delimeters():

    out = format_comments_after_cell_delimeters("# %%some comment")
    assert out == "# %% some comment"

    out = format_comments_after_cell_delimeters("# %%     another comment")
    assert out == "# %% another comment"


def test_remove_empty_cells():
    # single empty cell
    out = remove_empty_cells("# %%\n\n# %%")
    assert out == "# %%"

    # single empty cell with comment
    out = remove_empty_cells("# %% comment\n\n# %%")
    assert out == "# %% comment"

    # two empty cells with comment
    out = remove_empty_cells("# %% comment\n\n# %%\n\n# %%")
    assert out == "# %% comment"

    # two empty cells with comment and spaces
    out = remove_empty_cells("# %% comment\n  \n   # %%\n  \n  # %%")
    assert out == "# %% comment"


def test_remove_empty_lines_starting_cell():
    # cell with single blank line between cell delimeter and first code line
    out = remove_empty_lines_starting_cell("# %%\n\nfoo = 'bar'")
    assert out == "# %%\nfoo = 'bar'"

    # cell with 4 blank lines between cell delimeter and first code line
    out = remove_empty_lines_starting_cell("# %%\n\n\n\nfoo = 'bar'")
    assert out == "# %%\nfoo = 'bar'"

    # cell with 4 blank and spaces lines between cell delimeter and first code line
    out = remove_empty_lines_starting_cell("# %%\n\t\t\n  \n    \nfoo = 'bar'")
    assert out == "# %%\nfoo = 'bar'"


def test_ensure_two_blank_lines_preceding_cell():
    # single preceding blank line
    out = ensure_two_blank_lines_preceding_cell("\n# %%\n")
    assert out == "\n\n\n# %%\n"

    # single preceding blank line with code in cell
    out = ensure_two_blank_lines_preceding_cell("\n# %%\nfoo = 'bar'")
    assert out == "\n\n\n# %%\nfoo = 'bar'"

    # too many preceding blank line with code in cell
    out = ensure_two_blank_lines_preceding_cell("\n\n\n\n\n\n# %%\nfoo = 'bar'")
    assert out == "\n\n\n# %%\nfoo = 'bar'"


def test_delete_last_cell_if_empty():
    # empty last cell containing single blank line
    out = delete_last_cell_if_empty("\n# %%\na = 5\n\n\n# %%\n")
    assert out == "\n# %%\na = 5\n"

    # empty last cell containing many blank lines
    out = delete_last_cell_if_empty("\n# %%\na = 5\n\n\n# %%\n\n\n\n")
    assert out == "\n# %%\na = 5\n"

    # empty last cell containing many blank lines + other white space
    out = delete_last_cell_if_empty("\n# %%\na = 5\n\n\n# %%\n\t  \n\n   \n")
    assert out == "\n# %%\na = 5\n"
