import pytest
from cards import Card

def test_with_fail():
    c1 = Card("Sit there", "Brian")
    c2 = Card("Do something", "Okken")
    if c1 != c2:
        pytest.fail("They don't match")
