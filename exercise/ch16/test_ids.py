import pytest
from cards import Card


@pytest.mark.parametrize("start_state", ["done", "in prog", "todo"])
def test_finish(cards_db, start_state):
    index = cards_db.add_card(Card("some task", state=start_state))
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


@pytest.mark.parametrize(
    "starting_card",
    [
        Card("some task", state="todo"),
        Card("some task", state="in prog"),
        Card("some task", state="done"),
    ],
)
def test_card(cards_db, starting_card):
    index = cards_db.add_card(starting_card)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


card_list = [
    Card("some task", state="todo"),
    Card("some task", state="in prog"),
    Card("some task", state="done"),
]

@pytest.mark.parametrize("starting_card", card_list, ids=str)
def test_id_str(cards_db, starting_card):
    index = cards_db.add_card(starting_card)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


def card_state(card: Card) -> str:
    return card.state


@pytest.mark.parametrize("starting_card", card_list, ids=card_state)
def test_id_func(cards_db, starting_card):
    index = cards_db.add_card(starting_card)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


@pytest.mark.parametrize("starting_card", card_list, ids=lambda c: c.state)
def test_id_lamda(cards_db, starting_card):
    index = cards_db.add_card(starting_card)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


card_list_with_param = [
    Card("some task", state="todo"),
    pytest.param(Card("some task", state="in prog"), id="special"),
    Card("some task", state="done"),
]


@pytest.mark.parametrize("starting_card", card_list_with_param, ids=card_state)
def test_id_param(cards_db, starting_card):
    index = cards_db.add_card(starting_card)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


id_list = ["todo from_id_list", "in prog from_id_list", "done from_id_list"]
@pytest.mark.parametrize("starting_card", card_list, ids=id_list)
def test_id_list(cards_db, starting_card):
    index = cards_db.add_card(starting_card)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


text_variants = {
    "Short": "x",
    "With Spaces": "x y z",
    "End In Spaces": "x    ",
    "Mixed Case": "MiXeD cAsE",
    "Unicode": "你好世界",
    "New Lines": "a\nb\nc",
    "Tabs": "a\tb\tc",
}


@pytest.mark.parametrize(
    "variant", text_variants.values(), ids=text_variants.keys()
)
def test_summary_variants(cards_db, variant):
    i = cards_db.add_card(Card(summary=variant))
    c = cards_db.get_card(i)
    assert c.summary == variant
