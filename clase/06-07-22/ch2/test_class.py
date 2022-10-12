from cards import Card

class TestEquality:

    def test_equality_fail(self):
        c1 = Card("something", "brian", "todo", 123)
        c2 = Card("something", "brian", "todo", 123)
        assert c1 == c2

    def test_equality_width_diff_ids(self):
        c1 = Card("something", "brian",  "todo", 123)
        c2 = Card("something", "brian",  "todo", 123)
        assert c1 == c2