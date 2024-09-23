# To run all tests:
#     pytest -v -m all exercises/test_markers.py
# To run the odd tests:
#     pytest -v -m odd exercises/test_markers.py
# To run the odd tests that are not marked with testclass:
#     pytest -v -m "odd and not testclass" exercises/test_markers.py
# To run the odd tests that are parametrized:
#     pytest -v -m odd -k param exercises/test_markers.py
########################################################################
import pytest


pytestmark = [pytest.mark.all]


@pytest.mark.odd
def test_one():
    pass


def test_two():
    pass


@pytest.mark.odd
def test_three():
    pass


@pytest.mark.testclass
class TestClass:
    def test_four(self):
        pass

    @pytest.mark.odd
    def test_five(self):
        pass


@pytest.mark.parametrize("x", [
    6,
    pytest.param(7, marks=[pytest.mark.odd])])
def test_param(x):
    pass
