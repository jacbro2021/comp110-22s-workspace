"""Excercise 06 - Practice with Dictionaries."""

__author__ = "730461954"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Inverts a given dictionary."""
    invert_d: dict[str, str] = {}
    for key in x:
        invert_d[x[key]] = key 
    if len(invert_d) != len(x):
        raise KeyError("Error! there are multiple values with the same key.")
    else:
        return invert_d


def favorite_color(x: dict[str, str]) -> str:
    """Finds the favorite color in a dictionary."""
    y: dict[str, int] = {}
    for key in x:
        if x[key] in y:
            y[x[key]] += 1
        else:
            y[x[key]] = 1
    favorite_color: str = ""
    for color in y:
        if favorite_color == "":
            favorite_color = color
        if y[color] > y[favorite_color]:
            favorite_color = color
    return favorite_color


def count(x: list[str]) -> dict[str, int]:
    """Creates a dictionary that counts the number of times each item is in a list."""
    y: dict[str, int] = {}
    i: int = 0
    while i < len(x):
        if x[i] in y: 
            y[x[i]] += 1
        else:
            y[x[i]] = 1
        i += 1
    return y
