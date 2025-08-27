from typer.testing import CliRunner

from agent_space.cli import app

runner = CliRunner()


def test_cli_list() -> None:
    result = runner.invoke(app, ["list", "tools"])
    assert result.exit_code == 0
    assert "browser" in result.stdout


def test_cli_run() -> None:
    result = runner.invoke(app, ["run", "groupchat", "hello"])
    assert result.exit_code == 0
    assert "hello" in result.stdout
