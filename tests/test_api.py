import pytest

from cronpar.api import _parse_str


@pytest.mark.parametrize(
    "input_str,_type,expected",
    [
        ("*/15", "minute", [0, 15, 30, 45]),
        ("0,12", "hour", [0, 12]),
        ("1,15", "day of month", [1, 15]),
        ("*/3", "month", [3, 6, 9, 12]),
        ("1-5", "day of week", list(range(1, 6))),
    ],
)
def test_parse(input_str, _type, expected):
    res = _parse_str(input_str, _type)
    assert res == expected


def test_if_invalid_str():
    with pytest.raises(ValueError):
        _parse_str("invalid", "month")
