import shlex
from typer.testing import CliRunner
from cards.cli import app


runner = CliRunner()


def cards_cli(command_string):
    command_list = shlex.split(command_string)
    result = runner.invoke(app, command_list)
    output = result.stdout.rstrip()
    return output


def test_cards_cli():
    result = cards_cli("version")
    print()
    print(f"version: {result}")

    result = cards_cli("list -o brain")
    print(f"list:\n{result}")
