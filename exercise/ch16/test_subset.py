import pytest
from cards import Card


@pytest.fixture(params=["admin", "team_member", "visitor"])
def user(request):
    role = request.param
    return role


def test_everyone(user):
    print(f"Test case for {user}.")


@pytest.mark.parametrize("user", ["admin"], indirect=["user"])
def test_just_admin(user):
    print(f"Test case just for {user}.")
