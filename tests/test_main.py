import filecmp
from importlib.metadata import version
from shutil import copy2

import pytest

from format_ipy_cells.main import main


def test_main_format_cells(capsys, tmpdir):
    clean_nb = "tests/fixtures/clean_nb.py"

    raw_file = copy2("tests/fixtures/raw_nb.py", tmpdir)
    # test we leave clean file as is and don't write logs about it
    clean_file = copy2(clean_nb, tmpdir)

    ret = main((raw_file, clean_file))

    assert ret == 1
    assert filecmp.cmp(raw_file, clean_nb), "Formatted file has unexpected content"
    assert filecmp.cmp(clean_file, clean_nb), "clean file should not have changed"

    out, err = capsys.readouterr()
    assert out == f"Rewriting {raw_file}\n"
    assert err == ""

    ret = main([clean_file])
    assert ret == 0, "expected exit code 0 when no files were changed"
    out, err = capsys.readouterr()
    assert out == err == ""


def test_main_print_version(capsys):

    with pytest.raises(SystemExit):
        ret_val = main(["-v"])
        assert ret_val == 0

    stdout, stderr = capsys.readouterr()

    fic_version = version("format-ipy-cells")

    assert stdout == f"format-ipy-cells v{fic_version}\n"
    assert stderr == ""
