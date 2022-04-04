from __future__ import annotations
from typing import Union


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        """Docstring."""
        self.items = items

    def __repr__(self) -> str:
        """Docstring."""
        return f"StrArray({self.items}"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        """Vectorized concatination operator."""
        a_list: list[str] = []

        if isinstance(rhs, str):
            for item in self.items:
                a_list.append(item + rhs)
        else:
            for i in range(0, len(self.items)):
                a_list.append(self.items[i] + rhs.items[i])
        
        return StrArray(a_list)


first: StrArray = StrArray(["Armando", "Brady", "Caleb"])
last: StrArray = StrArray([" Bacot", " Manek", " Love"])
result: StrArray = first + " natty champ " + last
print(result)
print(first + last)