"""Lesson on Recursion."""

from __future__ import annotations
from typing import Optional


class Node:
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Initializes Node objects."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Magic Hoodini man."""
        if self.next is None:
            return f"{self.data} -> bing-bong"
        else:
            return f"{self.data} -> {self.next}"


def sum(node: Optional[Node]) -> int:
    if node is None:
        return 0  # When writing a recursive function, you will always need a base case
    else:
        return node.data + sum(node.next)  # A recursive functions will also always have a recursive case.
        # There can be multiple recursive cases in a recursive funtion.


def count(node: Optional[Node], current_count: int = 0) -> int:
    if node is None:
        return current_count
    else:
        return count(node.next, current_count + 1)
    

head: Node = Node(3, None)   
head = Node(2, head)
head = Node(1, head)
print(sum(head))
print(count(head))
print(head)
