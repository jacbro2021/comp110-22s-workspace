"""Utility class for numerical operations."""

from __future__ import annotations
from typing import Union

__author__ = "730461954"


class Simpy:
    """A class that will have various uses."""
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, values: list[float]):
        """Intializes new objects."""
        self.values = values

    def __str__(self) -> str:
        """A method that takes no arguments and returns a string."""
        return f"Simpy({self.values})"

    def fill(self, value: float, i: int) -> None:
        """Fills a simpy object with a given number of floats."""
        if len(self.values) != 0:
            self.values = []
        while len(self.values) < i:
            self.values.append(value)      
        return None     

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Mutates self and creates a list of numbers that increased from start to stop by given length steps."""
        assert step != 0.0
        if len(self.values) != 0:
            self.values = []
        self.values.append(start)
        while self.values[len(self.values) - 1] != stop - step:
            start += step
            self.values.append(start)
        return None

    def sum(self) -> float:
        """Finds the sum of a list."""
        i: int = 0
        result: float = 0.0
        while i < len(self.values):
            result += self.values[i]
            i += 1
        return result

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Vector concatination operator."""
        sum_list: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            for item in self.values:
                sum_list.append(item + rhs.values[i])
                i += 1
            return Simpy(sum_list)
        
        if isinstance(rhs, float):
            for item in self.values:
                sum_list.append(item + rhs)
            return Simpy(sum_list)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Vectors exponentiation operator."""
        pow_list: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            for item in self.values:
                pow_list.append(item ** rhs.values[i])
                i += 1
            return Simpy(pow_list)
        
        if isinstance(rhs, float):
            for item in self.values:
                pow_list.append(item ** rhs)
            return Simpy(pow_list)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Creates a mask equality."""
        new_bool: list[bool] = []
        if isinstance(rhs, Simpy):
            i: int = 0
            for item in self.values:
                if item == rhs.values[i]:
                    new_bool.append(True)
                else: 
                    new_bool.append(False)
                i += 1
        if isinstance(rhs, float):
            for item in self.values:
                if item == rhs:
                    new_bool.append(True)
                else:
                    new_bool.append(False)
        return new_bool

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Creates a mask for greater than."""
        new_bool: list[bool] = []
        if isinstance(rhs, Simpy):
            i: int = 0
            for item in self.values:
                if item > rhs.values[i]:
                    new_bool.append(True)
                else: 
                    new_bool.append(False)
                i += 1
        if isinstance(rhs, float):
            for item in self.values:
                if item > rhs:
                    new_bool.append(True)
                else:
                    new_bool.append(False)
        return new_bool

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Adds ability to use subscription notation."""      
        if isinstance(rhs, int):
            sub: float = self.values[rhs]
            return sub
        if isinstance(rhs, list):
            boolin: list[bool] = []
            i: int = 0
            for item in self.values:
                if rhs[i] is True:
                    boolin.append(item)
                i += 1
            return Simpy(boolin)