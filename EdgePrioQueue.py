from queue import PriorityQueue
from abc import abstractmethod


class EdgePQ:
    def __init__(self):
        self.queue = PriorityQueue()

    @abstractmethod
    def insert(self, edge):
        pass

    @abstractmethod
    def remove(self):
        pass

    def isEmpty(self):
        return self.queue.empty()
