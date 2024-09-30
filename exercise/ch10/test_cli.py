import pytest
import shlex
import cards
from cards import app
from typer.testing import CliRunner
from unittest.mock import patch


runner = CliRunner()


def cards_cli(command_string):
    command_list = shlex.split(command_string)
    result = runner.invoke(app, command_list)
    output = result.stdout.rstrip()
    return output


@pytest.fixture
def mock_cardsdb():
    with patch.object(cards, "CardsDB", autospec=True) as MockCardsDB:
        db = MockCardsDB.return_value
        yield db


def test_add_with_owner(mock_cardsdb):
    cards_cli("add some task -o brian")
    expected = cards.Card("some task", owner="brian", state="todo")
    mock_cardsdb.add_card.assert_called_with(expected)


def test_delete_invalid(mock_cardsdb):
    mock_cardsdb.delete_card.side_effect = cards.api.InvalidCardId
    out = cards_cli("delete 25") # random invalid id
    assert "Error: Invalid card id 25" in out
