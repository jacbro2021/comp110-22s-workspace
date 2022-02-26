"""Unit testing for Utils."""

__author__ = """730461954"""

from utils import only_evens
from utils import sub
from utils import concat

"""Only_Even test functions"""


def test_only_evens_evens() -> None:
    """Ensures that only_evens properly returns even numbers."""
    x: list[int] = [2, 4, 6]
    assert only_evens(x) == [2, 4, 6]
    

def test_only_evens_odds() -> None:
    """Ensures that only_even does not return odds."""
    x: list[int] = [1, 3, 5, 7]
    assert only_evens(x) == []


def test_only_evens_edge() -> None:
    """Tests to see if only_evens works with any number."""
    x: list[int] = [1, 10000000]
    assert only_evens(x) == [10000000]


"""Sub test functions."""


def test_sub() -> None:
    """Tests to see if sub can return the first half of a list."""
    x: list[int] = [1, 2, 3, 4]
    assert sub(x, -12, 2) == [1, 2]


def test_sub_normal() -> None:
    """Tests to see if sub properly returns the latter half of a list."""
    x: list[int] = [1, 2, 3, 4]
    assert sub(x, 2, 4) == [3, 4]


def test_sub_edge() -> None:
    """Tests to see if sub can correctly handle negative inputs and single value lists."""
    x: list[int] = [1]
    assert sub(x, -100, 1) == [1]


"""Concat test functions."""


def test_concat_normal() -> None:
    """Tests concat to see if it returns the proper concatenation."""
    x: list[int] = [10, 20, 30]
    y: list[int] = [40, 50, 60]
    assert concat(x, y) == [10, 20, 30, 40, 50, 60]


def test_concat_disorder() -> None:
    """Tests concat to see if values are returned in the correct order."""
    x: list[int] = [10, 30, 70]
    y: list[int] = [20, 73, 45]
    assert concat(x, y) == [10, 30, 70, 20, 73, 45]


def test_concat_empty() -> None:
    """Tests concat with an empty list."""
    x: list[int] = []
    assert concat(x, x) == []