import pytest
import cards
from cards import Card
from packaging.version import parse


@pytest.mark.skipif(
    parse(cards.__version__).major < 2,
    reason="Card doesn't support < comparison in version 1.x",
)
def test_less_than():
    c1 = Card("a task")
    c2 = Card("b task")
    assert c1 < c2


def test_equality():
    c1 = Card("a task")
    c2 = Card("a task")
    assert c1 == c2
