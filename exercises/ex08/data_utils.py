"""Dictionary related utility functions."""

__author__ = "730461954"

from csv import DictReader

# Define your functions below


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []
    # open handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Read that file
    csv_reader = DictReader(file_handle)

    # read each row of the csv, line by line.
    for row in csv_reader:
        result.append(row)

    # close the file when we're done, to free its resources
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row oriented table to a column documented table."""
    result: dict[str, list[str]] = {}    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(columns: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produces a new column based table with only the first few rows of data."""
    new: dict[str, list[str]] = {}
    if n > len(columns):
        for key in columns:
            new[key] = columns[key]
        return new
    for column in columns:
        mini: list[str] = []
        i: int = 0 
        while i < n:
            mini.append(columns[column][i])
            i += 1
        new[column] = mini
    return new


def select(data: dict[str, list[str]], search: list[str]) -> dict[str, list[str]]:
    """Produces a new table with only a few of the original columns."""
    magnify: dict[str, list[str]] = {}
    for topic in search:
        for title in data:
            if topic == title:
                magnify[title] = data[title]
    return magnify


def concat(data_one: dict[str, list[str]], data_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column-based table with two column-based tables combined."""
    summed: dict[str, list[str]] = {}
    for column in data_one:
        summed[column] = data_one[column]
    for key in data_two:
        if key in summed:
            summed[key] += data_two[key]
        else:
            summed[key] = data_two[key]
    return summed


def count(x: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears in a list."""
    n: dict[str, int] = {}
    for item in x:
        if item in n:
            n[item] += 1
        else:
            n[item] = 1
    return n