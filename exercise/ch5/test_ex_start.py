from cards import Card


def test_start_from_done(cards_db):
    c = Card("Dummy summary", state="done")
    index = cards_db.add_card(c)
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"


def test_start_from_in_prog(cards_db):
    c = Card("Dummy summary", state="in prog")
    index = cards_db.add_card(c)
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"


def test_start_from_todo(cards_db):
    c = Card("Dummy summary", state="todo")
    index = cards_db.add_card(c)
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"
