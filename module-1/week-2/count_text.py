"""
Module: 1
Week: 2
HW: count words in text
"""


def count_text(path="P1_data.txt"):
    """
    Count the number of words in a text file.
    """
    with open(path, "r", encoding=str) as file:
        text = file.read()
        text = text.lower()
        text = text.replace("\n", " ")

    return {word: text.count(word) for word in text.split()}


# print(count_text())
