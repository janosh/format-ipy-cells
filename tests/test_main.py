from importlib.metadata import version

import pytest

from format_ipy_cells.main import main


def test_main_format_cells(capsys, tmpdir):

    with open("tests/fixtures/raw_nb.py") as file:
        raw_txt = file.read()

    with open("tests/fixtures/clean_nb.py") as file:
        clean_txt = file.read()

    # empty file to test we don't modify files needlessly
    file1 = tmpdir.join("file1.py").ensure()

    file2 = tmpdir.join("file2.py")
    file2.write(raw_txt)

    ret = main((str(file1), str(file2)))

    assert ret == 1
    assert file2.read() == clean_txt

    out, _ = capsys.readouterr()
    assert out == f"Rewriting {file2}\n"


def test_main_print_version(capsys):

    with pytest.raises(SystemExit):
        ret_val = main(["-v"])
        assert ret_val == 0

    stdout, stderr = capsys.readouterr()

    fic_version = version("format-ipy-cells")

    assert stdout == f"format-ipy-cells v{fic_version}\n"
    assert stderr == ""
