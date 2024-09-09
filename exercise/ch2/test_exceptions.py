import pytest
import cards


def test_no_path_raises():
    with pytest.raises(TypeError):
        cards.CardsDB()


def test_raises_with_info():
    match_regex = r"missing 1 .* positional argument"
    with pytest.raises(TypeError, match=match_regex):
        cards.CardsDB()


def test_raises_with_info_alt():
    with pytest.raises(TypeError) as e_info:
        cards.CardsDB()
    expected = "missing 1 required positional argument"
    assert expected in str(e_info.value)
