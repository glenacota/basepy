from . import initlog
from basepy import basepy


def test_success():
    # when
    result = basepy.run()
    # then
    assert result is True, "Should be True"


def test_log(caplog, initlog):
    # when
    basepy.run()
    # then
    expected_log = "All is good!"
    assert expected_log in caplog.text, f"Should log '{expected_log}'"
