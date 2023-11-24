import pytest
from one_hot import fit_transform


def test_args_list_str():
    """Test a function with arguments - list of strings"""
    assert fit_transform(['Moscow', 'Moscow', 'Moscow', 'London']) == [
            ('Moscow', [0, 1]),
            ('Moscow', [0, 1]),
            ('Moscow', [0, 1]),
            ('London', [1, 0]),
        ]


def test_args_str():
    """Test a function with arguments - strings"""
    assert fit_transform('Moscow', 'Moscow', 'Moscow', 'London') == [
            ('Moscow', [0, 1]),
            ('Moscow', [0, 1]),
            ('Moscow', [0, 1]),
            ('London', [1, 0]),
        ]


def test_args_list_int():
    """Test a function with arguments - list of integers"""
    assert fit_transform([1, 2, 2, 3]) == [
            (1, [0, 0, 1]),
            (2, [0, 1, 0]),
            (2, [0, 1, 0]),
            (3, [1, 0, 0]),
        ]


def test_args_list_float():
    """Test a function with arguments - list of floats"""
    assert fit_transform([1.5, 2.9, 3.4, 1.5]) == [
            (1.5, [0, 0, 1]),
            (2.9, [0, 1, 0]),
            (3.4, [1, 0, 0]),
            (1.5, [0, 0, 1]),
        ]


def test_args_empty():
    """Test a function with empty arguments"""
    with pytest.raises(TypeError):
        fit_transform()


def test_args_floats():
    """Test a function with arguments - floats"""
    with pytest.raises(TypeError):
        fit_transform(1.2, 3.4, 5.6)
