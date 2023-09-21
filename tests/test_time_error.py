from unittest.mock import Mock
from lib.time_error import TimeError

def test_time_error():
    requester = Mock(name="requester")
    response = Mock(name="response")
    timer = Mock(name="timer")

    requester.get.return_value = response

    response.json.return_value = {
        "abbreviation": "BST",
        "unixtime": 100
    }

    timer.time.return_value = 50

    time_error = TimeError(requester, timer)
    assert time_error.error() == 50