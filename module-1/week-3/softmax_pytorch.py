"""
Module: 1
Week: 3
HW: build softmax and softmax_stable functions with PyTorch
"""

import torch
from torch import nn


class Softmax(nn.Module):
    """
    Softmax function.
    """

    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        x = torch.exp(x) / torch.sum(torch.exp(x), dim=0)
        return x


class SoftmaxStable(nn.Module):
    """
    Stable Softmax function.
    """

    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        c = torch.max(x, dim=0)[0]
        x = torch.exp(x - c) / torch.sum(torch.exp(x - c), dim=0)
        return x


if __name__ == "__main__":
    x = torch.tensor([1, 2, 3])
    softmax = Softmax()
    print(softmax(x))

    softmax_stable = SoftmaxStable()
    print(softmax_stable(x))
