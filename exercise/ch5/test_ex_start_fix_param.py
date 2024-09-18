import pytest
from cards import Card


@pytest.fixture(params=["done", "in prog", "todo"])
def current_state(request):
    return request.param


def test_start(cards_db, current_state):
    c = Card(summary="dummy summary", state=current_state)
    index = cards_db.add_card(c)
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"
