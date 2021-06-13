import re
from argparse import ArgumentParser
from importlib.metadata import version
from typing import Optional, Sequence


# use re.MULTILINE flag (equals inline modifier (?m)) to make ^ and $ match
# and start/end of each line instead of just start/end of whole string
# https://docs.python.org/3/library/re.html#re.MULTILINE


def format_cell_delimeters(text: str) -> str:
    """Ensure single space between hash and double-percent.

    --- before ---
    #   %%
    #%%
    --- after ---
    # %%
    # %%
    """
    return re.sub(r"(?m)^#\s*%%", r"# %%", text)


def format_comments_after_cell_delimeters(text: str) -> str:
    """Ensure single space between cell delimeter and possible comment on same line.

    --- before ---
    # %%some comment
    # %%     another comment
    --- after ---
    # %% some comment
    # %% another comment
    """
    # [^\S\n\r] = not non-whitespace and not new line or carriage return
    return re.sub(r"(?m)^# %%[^\S\n\r]*(\S)", r"# %% \g<1>", text)


def remove_empty_cells(text: str) -> str:
    """Remove empty cells.

    --- before ---
    # %% some comment

    # %%
    --- after ---
    # %% some comment
    """
    text = re.sub(r"(?m)^# %%(?:\s+# %%)+", r"# %%", text)
    return re.sub(r"(?m)^# %%([^\n]*)(?:\s+# %%$)+", r"# %%\g<1>", text)


def remove_empty_lines_starting_cell(text: str) -> str:
    """Remove empty lines from start of cell.

    --- before ---
    # %% comment

    first_code = 'here'
    --- after ---
    # %% comment
    first_code = 'here'
    """
    # (?:\n\s*){2,} = non-capturing group for two or more new lines containing
    # only optional white space
    return re.sub(r"(?m)^(# %%[^\n]*)(?:\n\s*){2,}", r"\g<1>\n", text)


def ensure_two_blank_lines_preceding_cell(text: str) -> str:
    """Ensure every cell delimeters has two preceding blank lines.
    Adds/deletes lines if there are less/more.

    --- before ---
    # %%
    some_code = 'here'
    # %%
    --- after ---
    # %%
    some_code = 'here'


    # %%
    """
    return re.sub(r"(?m)\n+^# %%", r"\n\n\n# %%", text)


def delete_last_cell_if_empty(text: str) -> str:
    """Delete last cell in file if it contains no code and no comment.

    --- before ---
    # %%
    some_code = 'here'

    # %%

    --- after ---
    # %%
    some_code = 'here'

    """
    # \Z matches only at end of string
    return re.sub(r"(?m)\s+^# %%\s*\Z", r"\n", text)


def format_cells(filename: str) -> None:
    with open(filename) as file:
        orig_text = text = file.read()

    # strip whitespace from start of file and from end of every line
    text = "\n".join(line.rstrip() for line in text.lstrip().split("\n"))

    text = format_cell_delimeters(text)

    text = format_comments_after_cell_delimeters(text)

    text = remove_empty_cells(text)

    text = remove_empty_lines_starting_cell(text)

    text = ensure_two_blank_lines_preceding_cell(text)

    text = ensure_two_blank_lines_preceding_cell(text)

    text = delete_last_cell_if_empty(text)

    with open(filename, "w") as file:
        file.write(text)

    if orig_text != text:
        print(f"Modified {filename}")


def main(argv: Optional[Sequence[str]] = None) -> int:

    parser = ArgumentParser("Format iPython Cells")

    fic_version = version("format-ipy-cells")
    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s v{fic_version}"
    )

    parser.add_argument("filenames", nargs="*", help="Filenames to format")

    args = parser.parse_args(argv)

    for filename in args.filenames:
        format_cells(filename)

    return 0


if __name__ == "__main__":
    exit(main())
