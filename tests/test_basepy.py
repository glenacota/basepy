from . import initlog
from click.testing import CliRunner
from basepy import basepy

runner = CliRunner()


def test_greet_subcommand_with_defaults():
    # when
    result = runner.invoke(basepy.run, ["greet"])
    # then
    assert result.exit_code == 0, "Should be 0"
    assert isinstance(result.output, str), "Should be a string"
    assert _count_lines(result.output) == 1, "Should be one line of output"
    assert result.output.startswith("Hello"), "Should start with a Hello"


def test_greet_subcommand_with_name():
    # when
    result = runner.invoke(basepy.run, ["greet", "-n", "Super Mario"])
    # then
    assert result.exit_code == 0, "Should be 0"
    assert _count_lines(result.output) == 1, "Should be one line of output"
    expected_greeting = "Hello, Super Mario!\n"
    assert expected_greeting == result.output, f"Should output '{expected_greeting}'"


def test_greet_subcommand_with_names():
    # when
    result = runner.invoke(basepy.run, ["greet", "-n", "Mario,Super Mario"])
    # then
    assert result.exit_code == 0, "Should be 0"
    assert _count_lines(result.output) == 2, "Should be two lines of output"
    expected_greeting = "Hello, Mario!\nHello, Super Mario!\n"
    assert expected_greeting == result.output, f"Should output '{expected_greeting}'"


def test_greet_like_a_pirate():
    # when
    result = runner.invoke(basepy.run, ["greet", "-n", "Guybrush Threepwood", "-p"])
    # then
    assert result.exit_code == 0, "Should be 0"
    assert _count_lines(result.output) == 1, "Should be one line of output"
    expected_greeting = "Ahoy, Guybrush Threepwood!\n"
    assert expected_greeting == result.output, f"Should output '{expected_greeting}'"


def test_log(caplog, initlog):
    # when
    runner.invoke(basepy.run, ["greet"])
    # then
    expected_log = "All is good!"
    assert expected_log in caplog.text, f"Should log '{expected_log}'"


def _count_lines(output):
    return output.count("\n")
