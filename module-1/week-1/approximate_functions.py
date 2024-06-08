"""
Module: 1
Week: 1
HW: Approximate sin, cos, sinh, cosh functions
"""


def factorial(n):
    """
    calculate the factorial of n
    """
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    return 1 if n == 0 else n * factorial(n - 1)


def approx_sin(x, n):
    """
    approximate sin(x)
    """
    result = 0
    for i in range(n):
        result += ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)

    return result


def approx_cos(x, n):
    """
    approximate cos(x)
    """
    result = 0
    for i in range(n):
        result += ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)

    return result


def approx_sinh(x, n):
    """
    approximate sinh(x)
    """
    result = 0
    for i in range(n):
        result += (x ** (2 * i + 1)) / factorial(2 * i + 1)

    return result


def approx_cosh(x, n):
    """
    approximate cosh(x)
    """
    result = 0
    for i in range(n):
        result += (x ** (2 * i)) / factorial(2 * i)

    return result


def main():
    """
    calculate and output the approximate values of sin, cos, sinh, cosh
    """
    x = input("x (rad): ")
    n = input("n (n > 0): ")

    print(f"sin({x}) = {approx_sin(x, n)}")
    print(f"cos({x}) = {approx_cos(x, n)}")
    print(f"sinh({x}) = {approx_sinh(x, n)}")
    print(f"cosh({x}) = {approx_cosh(x, n)}")
