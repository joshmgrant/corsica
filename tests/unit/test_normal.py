import pytest
from corsica.distributions import normal


def test_basic_inputs():
    vals = normal(10)
    assert len(vals) == 10

def test_empty_mu():
    with pytest.raises(TypeError):
        vals = normal(10,None,1)

def test_empty_sigma():
    with pytest.raises(TypeError):
        vals = normal(10,0,None)

def test_empty_both():
    with pytest.raises(TypeError):
        vals = normal(10,None,None)
