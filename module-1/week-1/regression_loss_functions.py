"""
Module: 1
Week: 1
HW: Regression Loss Functions
"""

from math import sqrt
import random


def loss(y, y_hat, loss_name):
    """
    return the loss value based on the loss function name
    """
    if loss_name == "mae":
        return abs(y - y_hat)
    if loss_name == "mse":
        return (y - y_hat) ** 2
    if loss_name == "rmse":
        return sqrt((y - y_hat) ** 2)

    raise ValueError("Invalid loss function name")


def main():
    """
    select the number of samples and loss function name
    """
    num_sample = input("num samples:")
    if isinstance(num_sample, int) is False:
        raise ValueError("Input should be an integer")

    loss_name = input("mae | mse | rmse: ")
    if loss_name not in ["mae", "mse", "rmse"]:
        raise ValueError("Invalid loss function name")

    total_loss = 0
    for i in range(num_sample):
        y = random.uniform(0, 10)
        y_hat = random.uniform(0, 10)

        print(f"""loss name: {loss_name}, sample: {i}, pred: {y_hat}, target: {y},
            loss: {loss(y, y_hat, loss_name)}""")

        total_loss += loss(y, y_hat, loss_name)

    print(f"final {loss_name}: {total_loss / num_sample}")
