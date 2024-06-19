"""
Module: 1
Week: 2
HW: count characters in string
"""


def count_char(string):
    """
    Count the number of characters in a string.
    """
    return {char: string.count(char) for char in string}


print(count_char("Happiness"))
