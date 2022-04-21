"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730461954"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    else:
        if head.next is None:
            return head.data
        else:
            return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Finds a value at a given index."""
    if index < 0:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        if head is None:
            raise IndexError("Index is out of bounds on the list.")
        else:
            return head.data
    else:
        if head is None:
            raise IndexError("Index is out of bounds on the list.")
        else:
            return value_at(head.next, index - 1)


def max(head: Optional[Node]) -> int:
    """Finds the max value in a linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    else:
        if head.next is None:
            return head.data
        else:
            i: int = head.data 
            if i < max(head.next):
                return max(head.next)
            else: 
                return i


def linkify(items: list[int]) -> Optional[Node]:
    """Returns a string representation of a linked list."""
    if len(items) == 0:
        return None
    else:
        if len(items) == 1:
            linky = Node(items[0], None)
            return linky
        else:
            return Node(items[0], linkify(items[1:]))


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Scales a Node object by a given factor."""
    if head is None:
        return None
    else:
        return Node(head.data * factor, scale(head.next, factor))