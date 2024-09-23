import pytest


def test_no_marker(cards_db):
    assert cards_db.count() == 0


@pytest.mark.num_cards
def test_marker_with_no_param(cards_db):
    assert cards_db.count() == 0


@pytest.mark.num_cards(3)
def test_3_cards(cards_db):
    assert cards_db.count() == 3
    print()
    for c in cards_db.list_cards():
        print(c)


@pytest.mark.num_cards(10)
def test_10_cards(cards_db):
    assert cards_db.count() == 10
