from basic_functions import add, multiply


def test_add():
    """Test the add function"""
    assert add(2, 3) == 5


def test_multiply():
    """Test the multiply function"""
    assert multiply(2, 3) == 6
