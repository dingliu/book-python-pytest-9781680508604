"""
Test Cases
* `list` from an empty database
* `list` from a non-empty database
"""
import pytest
from cards import Card


@pytest.fixture
def orig():
    return [
        Card("foo"),
        Card("bar", owner="me"),
        Card("baz", owner="you", state="in prog"),
    ]


@pytest.fixture
def cards_db_with_several_cards(cards_db, orig):
    for c in orig:
        cards_db.add_card(c)
    return cards_db


def test_list_no_cards(cards_db):
    """Empty db, empty list"""
    assert cards_db.list_cards() == []


def test_list_several_cards(cards_db_with_several_cards, orig):
    """
    Given a variety of cards, make sure they get returned.
    """
    the_list = cards_db_with_several_cards.list_cards()

    assert len(the_list) == len(orig)
    for c in orig:
        assert c in the_list


def test_list_cards_with_owner(cards_db_with_several_cards):
    """Given a specific owner
        When listing the card(s) with this owner
        The returned cards should have the same owner
    """
    the_list = cards_db_with_several_cards.list_cards(owner="me")
    assert len(the_list) == 1
    assert isinstance(the_list[0], Card)
    assert the_list[0].owner == "me"


def test_list_cards_with_state(cards_db_with_several_cards):
    """Given a specific state
        when listing the card(s) with this state
        the returned result should have the specified state
    """
    the_list = cards_db_with_several_cards.list_cards(state="in prog")
    assert len(the_list) == 1
    assert isinstance(the_list[0], Card)
    assert the_list[0].state == "in prog"


def test_list_cards_with_owner_state(cards_db_with_several_cards):
    """Given a specific state and a specific owner
        when listing the card(s) with these specs
        the returned result should have the specified owner and state
    """
    the_list = cards_db_with_several_cards.list_cards(
        owner="you", state="in prog")
    assert len(the_list) == 1
    assert isinstance(the_list[0], Card)
    assert the_list[0].owner == "you"
    assert the_list[0].state == "in prog"
