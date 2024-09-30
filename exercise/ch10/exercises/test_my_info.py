from unittest.mock import patch
from my_info import home_dir


@patch("my_info.Path", autospec=True)
def test_home_dir_return_value(MockPath):
    MockPath.home.return_value = "/users/fake_user"
    assert home_dir() == "/users/fake_user"


@patch("my_info.Path", autospec=True)
def test_home_dir_function_call(MockPath):
    home_dir()
    MockPath.home.assert_called()
