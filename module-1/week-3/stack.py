"""
Module: 1
Week: 3
HW: stack
"""


class Stack:
    """
    Stack class.
    """

    def __init__(self, capacity=10):
        self.__stack = []
        self.__capacity = capacity

    def is_empty(self):
        return len(self.__stack) == 0

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def pop(self):
        if self.is_empty():
            raise Exception("Stack underflow.")
        return self.__stack.pop()

    def push(self, item):
        if self.is_full():
            raise Exception("Stack overflow.")
        self.__stack.append(item)

    def top(self):
        if self.is_empty():
            return None
        return self.__stack[-1]
