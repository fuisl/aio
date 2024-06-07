"""
Module: 1
Week: 1
HW: activation functions
"""

# import numpy as np
from math import e


def is_number(n):
    """
    check if input is a number.
    """
    try:
        float(n)

    except ValueError:
        return False
    return True


def sigmoid(x):
    """
    Calculate sigmoid function.
    """
    return 1 / (1 + e**-x)


def relu(x):
    """
    Calculate ReLU function.
    """
    return x if x > 0 else 0


def elu(x, alpha=1):
    """
    Calculate ELU function.
    """
    return x if x > 0 else alpha * (e**x - 1)


def fx(x, func: str):
    """
    params:

    x: input value
    func (str): activation functions [sigmoid, relu, elu]

    """
    return func(x)


def main():
    """
    input and output
    """

    func = input("Input activation function (sigmoid | relu | elu): ")
    if func not in ["sigmoid", "relu", "elu"]:
        raise ValueError(f"{func} is not supported.")

    x = input("Input value: ")
    if not is_number(x):
        raise ValueError("x must be a number.")

    print(fx(float(x), func))
