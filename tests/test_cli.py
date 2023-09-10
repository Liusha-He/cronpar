import pytest

from cronpar.cli import run_explain


def test_if_input_is_valid():
    input_str = "*/15 0 1,15 * 1-5 /usr/bin/find"
    with pytest.raises(SystemExit) as e:
        run_explain([input_str])
        assert e.value.code == 0


def test_if_input_str_is_invalid():
    input_str = "whatever come in"
    with pytest.raises(ValueError):
        run_explain([input_str])
