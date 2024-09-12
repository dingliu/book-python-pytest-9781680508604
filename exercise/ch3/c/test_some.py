def test_add_some(cards_db, some_cards):
    expected_count = len(some_cards)
    for card in some_cards:
        cards_db.add_card(card)
    assert cards_db.count() == expected_count

def test_non_empty(non_empty_db):
    assert non_empty_db.count() > 0
