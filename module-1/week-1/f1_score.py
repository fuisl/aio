"""
Module: 1
Week: 1
HW: calculate F1 score
"""


def calculate_f1_score(tp, fp, fn):
    """
    Calculate F1 score with type check and value check for input.
    """
    if (
        isinstance(tp, int) is False
        or isinstance(fp, int) is False
        or isinstance(fn, int) is False
    ):
        raise TypeError("input must be type int")

    if tp < 0 or fp < 0 or fn < 0:
        raise ValueError("tp and tp and fn must be positive")

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)

    return f1_score
