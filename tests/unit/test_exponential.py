import pytest
from corsica.distributions import exponential


def test_basic_inputs():
    vals = exponential(10)
    assert all(x > 0 for x in vals)


def test_negative_lambda():
    with pytest.raises(TypeError):
        exponential(-1.0)


def test_empty_lambda():
    with pytest.raises(TypeError):
        exponential(None)
