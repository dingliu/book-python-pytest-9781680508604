# testing at multiple layers to avoid mocking
import shlex
import cards
import pytest
from cards import app
from typer.testing import CliRunner
from unittest.mock import patch


@pytest.fixture(scope="module")
def db_path(tmp_path_factory):
    db_path = tmp_path_factory.mktemp("cards_db")
    return db_path


@pytest.fixture(scope="function")
def cards_db(db_path, monkeypatch):
    monkeypatch.setenv("CARDS_DB_DIR", str(db_path))
    db = cards.CardsDB(db_path)
    db.delete_all()
    yield db
    db.close()



def cards_cli(command_string):
    runner = CliRunner()

    command_list = shlex.split(command_string)
    result = runner.invoke(app, command_list)
    output = result.stdout.rstrip()
    return output


def test_add_with_owner(cards_db):
    """A card shows up in the list with expected contents.
    """
    cards_cli("add some task -o brian")
    expected = cards.Card("some task", owner="brian", state="todo")
    all_cards = cards_db.list_cards()
    assert len(all_cards) == 1
    assert all_cards[0] == expected
