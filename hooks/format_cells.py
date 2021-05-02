import re
from argparse import ArgumentParser
from typing import Optional, Sequence

from importlib_metadata import version


def format_cells(filename: str) -> None:
    with open(filename) as file:
        orig_text = text = file.read()

    # use re.MULTILINE flag (equals inline modifier (?m)) to make ^ and $ match
    # and start/end of each line instead of just start/end of whole string
    # https://docs.python.org/3/library/re.html#re.MULTILINE

    # ensure single space between hash and double-percent
    # ---
    # #   %%
    # >>>
    # # %%
    # ---
    text = re.sub(r"(?m)^#\s*%%", r"# %%", text)

    # ensure single space between cell delimeter and possible comment on same line
    # ---
    # # %%some comment
    # # %%     some comment
    # >>>
    # # %% some comment
    # # %% some comment
    # ---
    # delete if more than 1
    text = re.sub(r"(?m)^# %%[^\S\r\n]{2,}(\S)", r"# %% \g<1>", text)
    # insert 1 if none
    text = re.sub(r"(?m)^# %%(\S)", r"# %% \g<1>", text)

    # remove empty cells
    # ---
    # # %% some comment
    #
    # # %%
    # >>>
    # # %% some comment
    # ---
    text = re.sub(r"(?m)^# %%([^\n]+)(?:\s+# %%[^ ])+", r"# %%\g<1>", text)

    # remove empty lines from start of cell
    # ---
    # # %%
    #
    # first_code = 'here'
    # >>>
    # # %%
    # first_code = 'here'
    # ---
    text = re.sub(r"(?m)^# %%([^\n]+)\n{2,}", r"# %%\g<1>\n", text)

    # ensure every cell delimeters has two preceding blank lines
    # adds/deletes lines if there are less/more
    # ---
    # # %%
    # some_code = 'here'
    # # %%
    # >>>
    # # %%
    # some_code = 'here'
    #
    #
    # # %%
    # ---
    text = re.sub(r"(?m)\n+^# %%", r"\n\n\n# %%", text)

    # delete last cell in file if it contains no code and no comment
    # ---
    # # %%
    # some_code = 'here'
    #
    # # %%
    #
    # >>>
    # # %%
    # some_code = 'here'
    #
    # ---
    text = re.sub(r"(?m)\s+^# %%\s*\Z", r"\n", text)

    # strip empty lines from start of file
    # ---
    #
    # # %%
    # >>>
    # # %%
    # ---
    text = text.lstrip()

    with open(filename, "w") as file:
        file.write(text)

    if orig_text != text:
        print(f"Modified {filename}")
    else:
        print(f"Nothing to do in {filename}")


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = ArgumentParser("Format iPython Cells")

    fic_version = version("format-ipy-cells")
    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {fic_version}"
    )

    parser.add_argument("filenames", nargs="*", help="Filenames to format")

    args = parser.parse_args(argv)

    for filename in args.filenames:
        format_cells(filename)


if __name__ == "__main__":
    exit(main())
