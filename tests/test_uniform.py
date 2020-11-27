import pytest
from corsica.distributions import uniform


def test_basic_inputs():
    vals = uniform(10)
    assert all(x > 0 for x in vals)
    assert all(x < 1 for x in vals)

def test_new_boundaries():
    vals = uniform(10,2,4)
    assert all(x > 2 for x in vals)
    assert all(x < 4 for x in vals)

def test_empty_lower():
    with pytest.raises(TypeError):
        vals = uniform(1,None,1)

def test_empy_upper():
    with pytest.raises(TypeError):
        vals = uniform(10,0,None)

def test_empty_both():
    with pytest.raises(TypeError):
        vals = uniform(10,None,None)

def test_equal_boundaries():
    with pytest.raises(ValueError):
        vals = uniform(10, 1.0, 1.0)

def test_swapped_boundaries():
    vals = uniform(10,5,3)
    assert all(x > 3 for x in vals)
    assert all(x < 5 for x in vals)
    
