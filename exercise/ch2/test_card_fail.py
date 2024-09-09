from cards import Card


def test_equality_fail():
    c1 = Card("Sit there", "Brian")
    c2 = Card("Do something", "Okken")
    assert c1 == c2
