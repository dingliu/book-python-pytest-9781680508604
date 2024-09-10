from cards import Card


class TestEquality:
    def test_equality(self):
        c1 = Card("Something", "Brian", "todo", 123)
        c2 = Card("Something", "Brian", "todo", 123)
        assert c1 == c2


    def test_equality_with_diff_ids(self):
        c1 = Card("Something", "Brian", "todo", 123)
        c2 = Card("Something", "Brian", "todo", 456)
        assert c1 == c2


    def test_inequality(self):
        c1 = Card("Something", "Brian", "todo", 123)
        c2 = Card("Different", "Okken", "done", 123)
        assert c1 != c2
