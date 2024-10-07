import pytest
from cards import Card


def text_variants():
    variants = {
        "Short": "x",
        "With Spaces": "x y z",
        "End In Spaces": "x    ",
        "Mixed Case": "MiXeD cAsE",
        "Unicode": "你好世界",
        "New Lines": "a\nb\nc",
        "Tabs": "a\tb\tc",
    }
    for key, value in variants.items():
        yield pytest.param(value, id=key)


@pytest.mark.parametrize("variant", text_variants())
def test_summary_rom_generator(cards_db, variant):
    i = cards_db.add_card(Card(summary=variant))
    c = cards_db.get_card(i)
    assert c.summary == variant
