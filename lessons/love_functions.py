"""Some examples of tender, loving functions."""


def love(name: str) -> str:
    """given a name as a parameter, returns a loving string"""
    return f"{name} es muy guapo"


def spread_love(to: str, n: int) -> str: 
    """generates a string that repeats a loving message n times"""
    love_note: str = str("")
    i: int = 0 
    while i <= n:
        love_note = str("I love you" + to + "\n")
        i += i + 1 
    return love_note 