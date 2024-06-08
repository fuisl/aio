"""
Module: 1
Week: 1
HW: implement tính diff nth root error for a pair (y, y_hat)
"""


def nth_root(x, n):
    """
    calculate the nth root of x. assume x >= 0
    """
    if x < 0:
        raise ValueError("x is assumed to be non-negative")
    return x ** (1 / n)


def md_diff_nth_root_error(y, y_hat, n, p):
    """
    calculate the nth root error of y and y_hat
    """
    return (nth_root(y, n) - nth_root(y_hat, n)) ** p


# print(md_diff_nth_root_error(100, 99.5, 2, 1))
