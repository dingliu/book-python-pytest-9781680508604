import pytest
from cards import Card


@pytest.fixture(scope="function")
def cards_db(db):
    db.delete_all()
    return db


@pytest.fixture(scope="function")
def cards_db_3_cards(db):
    db.delete_all() # start with empty
    # add three cards
    db.add_card(Card("Learn something new"))
    db.add_card(Card("Build useful tools"))
    db.add_card(Card("Teach others"))
    return db


def test_0_card(cards_db):
    assert cards_db.count() == 0


def test_3_cards(cards_db_3_cards):
    cards_db = cards_db_3_cards
    assert cards_db.count() == 3
