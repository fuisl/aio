"""
Module: 1
Week: 1
HW: activation functions
"""

import numpy as np


def sigmoid(x):
    """
    Calculate sigmoid function.
    """
    return 1 / (1 + np.exp(-x))


def relu(x):
    """
    Calculate ReLU function.
    """
    return x if x > 0 else 0


def elu(x, alpha=1):
    """
    Calculate ELU function.
    """
    return x if x > 0 else alpha * (np.exp(x) - 1)


def fx(x, func: str):
    """
    params:

    x: input value
    func (str): activation functions [sigmoid, relu, elu]

    """
    return func(x)
