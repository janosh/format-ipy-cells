from __future__ import annotations

import importlib.metadata as md
from argparse import ArgumentParser
from typing import Sequence

from format_ipy_cells.helpers import (
    delete_last_cell_if_empty,
    ensure_two_blank_lines_preceding_cell,
    format_cell_delimiters,
    format_comments_after_cell_delimiters,
    remove_empty_cells,
    remove_empty_lines_starting_cell,
)


def fix_file(filename: str) -> int:
    """Open specified file, apply all helper functions to format ipython cells
    and write changes back to file.

    Args:
        filename (str): File to format.
    """
    with open(filename) as file:
        orig_text = text = file.read()

    # strip whitespace from start of file and from end of every line
    text = "\n".join(line.rstrip() for line in text.lstrip().split("\n"))

    text = format_cell_delimiters(text)

    text = format_comments_after_cell_delimiters(text)

    text = remove_empty_cells(text)

    text = remove_empty_lines_starting_cell(text)

    text = ensure_two_blank_lines_preceding_cell(text)

    text = ensure_two_blank_lines_preceding_cell(text)

    text = delete_last_cell_if_empty(text)

    if orig_text != text:
        print(f"Rewriting {filename}")

        with open(filename, "w") as file:
            file.write(text)

        return 1
    return 0


def main(argv: Sequence[str] = []) -> int:
    """The format-ipy-cells CLI interface.

    Returns:
        int: 0 if format-ipy-cells exits successfully else returns an error code.
    """
    parser = ArgumentParser()

    pkg_version = md.version(pkg_name := "format-ipy-cells")
    parser.add_argument(
        "-v", "--version", action="version", version=f"{pkg_name} v{pkg_version}"
    )

    parser.add_argument("filenames", nargs="*", help="Filenames to format")

    args = parser.parse_args(argv)

    exit_code = 0

    for filename in args.filenames:
        exit_code |= fix_file(filename)

    return exit_code


if __name__ == "__main__":
    raise SystemError(main())
