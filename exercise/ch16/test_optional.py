import pytest


@pytest.fixture
def user(request):
    """Default role `visitor` is used when not indirectly parametrized."""
    role = getattr(request, 'param', 'visitor')
    print(f"\nLog in as {role}.")
    yield role
    print(f"\nLog out as {role}.")


def test_unspecified_user(user):
    print(f"Test case for {user}.")


@pytest.mark.parametrize("user", ["admin", "team_member"], indirect=["user"])
def test_admin_and_team_member(user):
    print(f"Test case for {user}.")
