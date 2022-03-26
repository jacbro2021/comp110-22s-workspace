"""Examples of default parameters."""


def add(x: int, y: int = 0, z: int = 0) -> int:
    """Example of a defualt param where y and z are zero by default"""
    return x + y + z


# You can not place non default params after default param in parameter list of functions.

print(add(1))
print(add(1, 2, 3))