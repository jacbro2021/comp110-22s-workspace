"""Ex05."""

__author__ = "730461954"


def only_evens(x: list[int]) -> list[int]:
    """Returns a list with only even integers."""
    evens: list[int] = []
    for i in x:
        if (i % 2) == 0:
            evens.append(i)
    return evens


def sub(x: list[int], start: int, end: int) -> list[int]:
    """Returns a sub-list from a given list."""
    y: list[int] = []
    if start < 0:
        start = 0
    if end > len(x):
        end = len(x)
    if len(x) == 0 or start > len(x) or end <= 0:
        return y
    while start <= (end - 1):
        y.append(x[start])
        start += 1
    return y


def concat(x: list[int], y: list[int]) -> list[int]:
    """Returns a single list that is composed of two lists put together."""
    combined: list[int] = []
    for i in x:
        combined.append(i)
    for c in y:
        combined.append(c)
    return combined
