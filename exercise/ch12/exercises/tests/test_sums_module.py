import pytest
from src.sums import main
from argparse import Namespace
from unittest.mock import patch, mock_open


def test_sums_main_positive(capsys):
    mock_file_content = "122.45\n77.55\n"

    with patch("builtins.open", mock_open(read_data=mock_file_content)):
        main(Namespace(files=["data.txt"]))
        output = capsys.readouterr().out
        assert output.strip() == "200.00"


def test_sums_main_negative(capsys):
    mock_file_content = "-122.45\n-77.55\n"

    with patch("builtins.open", mock_open(read_data=mock_file_content)):
        main(Namespace(files=["data.txt"]))
        output = capsys.readouterr().out
        assert output.strip() == "-200.00"


def test_sums_main_mix(capsys):
    mock_file_content = "-87.55\n77.55\n"

    with patch("builtins.open", mock_open(read_data=mock_file_content)):
        main(Namespace(files=["data.txt"]))
        output = capsys.readouterr().out
        assert output.strip() == "-10.00"


def test_sums_main_empty(capsys):
    mock_file_content = ""

    with patch("builtins.open", mock_open(read_data=mock_file_content)):
        main(Namespace(files=["data.txt"]))
        output = capsys.readouterr().out
        assert output.strip() == "0.00"


def test_sums_main_multiple_files(capsys):
    mock_file_content = "87.55\n-77.55\n"

    with patch("builtins.open", mock_open(read_data=mock_file_content)):
        main(Namespace(files=["data.txt", "data2.txt", "data3.txt"]))
        output = capsys.readouterr().out
        assert output.strip() == "30.00"


@patch("builtins.open")
def test_sums_main_nonexistent_file(mock_open):
    mock_open.side_effect = FileNotFoundError
    with pytest.raises(FileNotFoundError):
        main(Namespace(files=["data.txt"]))
