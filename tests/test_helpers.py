import pytest
from . import initlog
from basepy.helpers import greet, DEFAULT_NAMES


@pytest.mark.parametrize(
    "test_name",
    ["Mario", "Super Mario", "S1?"],
)
def test_greet_when_given_a_name(test_name):
    assert greet(test_name) == f"Hello, {test_name}!", "Should greet differently"


def test_greet_when_no_name_is_given():
    # when
    greeting = greet()
    # then
    assert any(name in greeting for name in DEFAULT_NAMES), "Should greet a default name"


@pytest.mark.parametrize(
    "test_pirate_name",
    ["Guybrush Threepwood", "Elaine Marley", "LeChuck", "Aaaarr!"],
)
def test_greet_pirates_when_given_a_name(test_pirate_name):
    # when
    greeting = greet(test_pirate_name, as_a_pirate=True)
    # then
    assert greeting == f"Ahoy, {test_pirate_name}!", "Should greet pirates differently"


def test_logs_greet_when_given_a_name(caplog, initlog):
    # when
    greet()
    # then
    assert not caplog.text, "Shouldn't log anything"


def test_logs_greet_pirates_when_given_a_name(caplog, initlog):
    # when
    greet(as_a_pirate=True)
    # then
    expectedLog = "Pirate mode!"
    assert expectedLog in caplog.text, f"Should log '{expectedLog}'"
