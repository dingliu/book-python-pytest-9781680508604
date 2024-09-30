import cards
import pytest

from unittest import mock
from cards.cli import app
from typer.testing import CliRunner


runner = CliRunner()


def test_mock_version():
    with mock.patch.object(cards, "__version__", "1.2.3"):
        result = runner.invoke(app, ["version"])
        assert result.stdout.rstrip() == "1.2.3"


def test_mock_CardsDB(capsys):
    """mocking a class - CardsDB in (imported) cards package"""
    with capsys.disabled():
        with mock.patch.object(cards, "CardsDB") as MockCardsDB:
            print()
            print(f"         class:{MockCardsDB}")
            print(f"return_value:{MockCardsDB.return_value}")
            with cards.cli.cards_db() as db:
                print(f"         object:{db}")


def test_mock_path(capsys):
    """mocking a method of a class - CardsDB.path()"""
    with capsys.disabled():
        with mock.patch.object(cards, "CardsDB") as MockCardsDB:
            MockCardsDB.return_value.path.return_value = "/foo/"
            with cards.cli.cards_db() as db:
                print()
                print(f"{db.path=}")
                print(f"{db.path()=}")


def test_bad_mock():
    with mock.patch.object(cards, "CardsDB") as MockCardsDB:
        db = MockCardsDB("/some/path")
        db.path() # good
        db.path() # invalid arguments
        db.not_valid() # invalid function


def test_good_mock():
    with mock.patch.object(cards, "CardsDB", autospec=True) as MockCardsDB:
        db = MockCardsDB("/some/path")
        db.path()
        with pytest.raises(TypeError):
            db.path(35)           # will raise TypeError
        with pytest.raises(AttributeError):
            db.invalid_function() # will raise AttributeError
