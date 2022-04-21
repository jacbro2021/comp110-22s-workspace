"""Tests for linked list utils."""


from exercises.ex10.linked_list import Node, last, value_at, linkify, scale
import pytest 

__author__ = "730461954"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise an value error."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return a reference to its last Node."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """An empty linked list should raise an error."""
    with pytest.raises(IndexError):
        value_at(None, 0)


def test_value_at_base() -> None:
    """Index 0 should return base data."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 0) == 1


def test_value_at_int() -> None:
    """Tests value_at function at a random iteration."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 2) == 3


def test_max_empty() -> None:
    """Raises error when given an empty node."""
    with pytest.raises(ValueError):
        max(None)


def test_max_regular() -> None:
    """Regular use test for max."""
    linked_list: Node = Node(10, Node(20, Node(30, None)))
    assert max(linked_list) == 30


def test_linkify_norm() -> None:
    """Normal use of linkify."""
    linked: list[int] = [1, 2, 3]
    assert str(linkify(linked)) == "1 -> 2 -> 3 -> None"


def test_linkify_empty() -> None:
    """Tests linkify with an empty list."""
    linked: list[int] = []
    assert linkify(linked) is None


def test_scale_uno() -> None:
    """Tests scale multiplying by 1."""
    assert str(scale(linkify([1, 2, 3]), 2)) == "2 -> 4 -> 6 -> None"


def test_scale_hunnid() -> None:
    """Tests scale multiplying by 100."""
    assert str(scale(linkify([1, 2, 3]), 100)) == "100 -> 200 -> 300 -> None"