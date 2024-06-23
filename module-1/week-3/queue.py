"""
Module: 1
Week: 3
HW: queue
"""


class Queue:
    """
    Queue class.
    """

    def __init__(self, capacity=10):
        self.__queue = []
        self.__capacity = capacity

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue underflow.")
        return self.__queue.pop(0)

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue overflow.")
        self.__queue.append(item)

    def front(self):
        if self.is_empty():
            return None
        return self.__queue[0]
