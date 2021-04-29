import re
from argparse import ArgumentParser
from typing import Optional, Sequence


def format_cells(filename: str) -> None:
    with open(filename) as file:
        text = file.read()

    # ensure every cell delimeters has two preceding blank lines
    # adds/deletes lines if there are less/more
    text = re.sub(r"\n*#\s*%%", r"\n\n\n# %%", text)

    # ensure number of spaces between cell delimeter and possible comment
    # on same line is 1
    text = re.sub(r"# %%[^\S\r\n]{2,}(\S)", r"# %% \g<1>", text)
    text = re.sub(r"# %%(\S)", r"# %% \g<1>", text)

    # strip empty lines from start of file
    text = text.lstrip()

    with open(filename, "w") as file:
        file.write(text)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = ArgumentParser("Format iPython Cells")

    parser.add_argument("filenames", nargs="*", help="Filenames to format")

    args = parser.parse_args(argv)

    print(f"{args=}")

    for filename in args.filenames:
        format_cells(filename)


if __name__ == "__main__":
    exit(main())
