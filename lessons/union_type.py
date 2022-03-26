"""An example of Union Types."""

from typing import Union


def log(info: Union[int, str]) -> None:
    """Log is a function that can be called with either an int or a str."""
    if isinstance(info, str):
        print(f"str: {info}")
    else:
        print(f"int: {info}")


log("Hello, World")
log(110)