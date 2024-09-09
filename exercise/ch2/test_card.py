from cards import Card


def test_field_access():
    c = Card("Something", "Brian", "todo", 123)
    assert c.summary == "Something"
    assert c.owner == "Brian"
    assert c.state == "todo"
    assert c.id == 123


def test_defaults():
    c = Card()
    assert c.summary is None
    assert c.owner is None
    assert c.state == "todo"
    assert c.id is None


def test_equality():
    c1 = Card("Something", "Brian", "todo", 123)
    c2 = Card("Something", "Brian", "todo", 123)
    assert c1 == c2


def test_equality_with_diff_ids():
    c1 = Card("Something", "Brian", "todo", 123)
    c2 = Card("Something", "Brian", "todo", 456)
    assert c1 == c2


def test_inequality():
    c1 = Card("Something", "Brian", "todo", 123)
    c2 = Card("Different", "Okken", "done", 123)
    assert c1 != c2


def test_from_dict():
    c1 = Card("Something", "Brian", "todo", 123)
    c2_dict = {
        "summary": "Something",
        "owner": "Brian",
        "state": "todo",
        "id": 123
    }
    c2 = Card.from_dict(c2_dict)
    assert c1 == c2


def test_to_dict():
    c1 = Card("Something", "Brian", "todo", 123)
    c1_dict = c1.to_dict()
    c1_expected = {
        "summary": "Something",
        "owner": "Brian",
        "state": "todo",
        "id": 123
    }
    assert c1_dict == c1_expected
