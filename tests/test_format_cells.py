from importlib.metadata import version
from shutil import copyfile

import pytest

from format_ipy_cells.main import main


raw_path = "tests/fixtures/raw_nb.py"
tmp_path = "tests/fixtures/tmp_nb.py"
clean_path = "tests/fixtures/clean_nb.py"


def test_format_cells():
    copyfile(raw_path, tmp_path)

    main([tmp_path])

    with open(tmp_path) as file:
        raw_fixed = file.read()

    with open(clean_path) as file:
        clean = file.read()

    assert (
        raw_fixed == clean
    ), f"formatted file '{tmp_path}' differs from target '{clean_path}'"


def test_main_print_version(capsys):

    fic_version = version("format-ipy-cells")

    with pytest.raises(SystemExit):
        main(["-v"])

    stdout, stderr = capsys.readouterr()

    fic_version = version("format-ipy-cells")

    assert stdout == f"Format iPython Cells v{fic_version}\n"
    assert stderr == ""
