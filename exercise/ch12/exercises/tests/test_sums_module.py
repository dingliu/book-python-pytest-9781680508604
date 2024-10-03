from src.sums import main
from argparse import Namespace


def test_sums_main(capsys):
    main(Namespace(files=["data.txt"]))
    output = capsys.readouterr().out
    assert output.strip() == "200.00"
