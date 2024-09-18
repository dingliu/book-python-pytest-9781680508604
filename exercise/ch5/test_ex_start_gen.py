from cards import Card


def pytest_generate_tests(metafunc):
    if "current_state" in metafunc.fixturenames:
        metafunc.parametrize("current_state", ["done", "in prog", "todo"])


def test_start(cards_db, current_state):
    c = Card(summary="dummy summary", state=current_state)
    index = cards_db.add_card(c)
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"

