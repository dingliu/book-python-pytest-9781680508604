import pytest
from cards import Card


summaries = ["short", "a bit longer"]
owners = ["First", "First M. Last"]
states = ["todo", "in prog", "done"]


@pytest.mark.parametrize("state", states)
@pytest.mark.parametrize("owner", owners)
@pytest.mark.parametrize("summary", summaries)
def test_stacking(cards_db, summary, owner, state):
    i = cards_db.add_card(Card(summary, owner, state))
    c = cards_db.get_card(i)
    expected = Card(summary, owner, state)
    assert c == expected
