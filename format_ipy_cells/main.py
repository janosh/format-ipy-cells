from argparse import ArgumentParser
from importlib.metadata import version
from typing import Optional, Sequence

from format_ipy_cells.helpers import (
    delete_last_cell_if_empty,
    ensure_two_blank_lines_preceding_cell,
    format_cell_delimeters,
    format_comments_after_cell_delimeters,
    remove_empty_cells,
    remove_empty_lines_starting_cell,
)


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
