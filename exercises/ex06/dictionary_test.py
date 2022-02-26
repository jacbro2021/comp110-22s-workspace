"""Unit testing for Ex06."""

__author__ = "730461954"

from dictionary import invert, favorite_color, count
import pytest

"""Unit Tests for invert function."""


def test_invert_normal() -> None:
    """Tests proper functionality for normal use.""" 
    x: dict[str, str] = {"1": "2", "3": "4"}
    assert invert(x) == {"2": "1", "4": "3"}


def test_invert_duplicate_key() -> None:
    """Tests proper response to duplicate keys."""
    with pytest.raises(KeyError):
        my_dictionary = {'U': 'NC', 'State': 'NC'}
        invert(my_dictionary)


def test_invert_empty() -> None:
    """Tests proper response to empty dictionary input."""
    x: dict[str, str] = {}
    assert invert(x) == {}


"""Unit Tests for favorite colors function."""


def test_favorite_colors_normal() -> None:
    """Tests normal use of favorite colors function."""
    x: dict[str, str] = {"johnny": "red", "jess": "red", "jacob": "blue"}
    assert favorite_color(x) == "red"


def test_favorite_color_tie() -> None:
    """Tests results of tie in normal color function."""
    x: dict[str, str] = {"j": "blue", "k": "red"}
    assert favorite_color(x) == "blue"


def test_favorite_color_randomness() -> None:
    """Tests results when the dictionary is more random."""
    x: dict[str, str] = {"johnny": "red", "jess": "yellow", "jacob": "blue", "shawna": "red"}
    assert favorite_color(x) == "red"


"""Unit Tests for count function."""


def test_count_normal() -> None:
    """Tests count function for normal use."""
    x: list[str] = ["j", "s", "y", "l", "y", "j"]
    assert count(x) == {"j": 2, "s": 1, "y": 2, "l": 1}


def test_count_empty() -> None:
    """Tests edge case for count of empty string."""
    x: list[str] = []
    assert count(x) == {}


def test_count_no_repeat() -> None:
    """Tests normal use with no repeated strings within list."""
    x: list[str] = ["j", "l", "r"]
    assert count(x) == {"j": 1, "l": 1, "r": 1}