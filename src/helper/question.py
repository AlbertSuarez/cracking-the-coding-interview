import abc
import time


class Question:

    __metaclass__ = abc.ABCMeta

    def __init__(self, name: str):
        self.name = name
        self.result = None

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, *args):
        self.end_time = time.time()
        self.total_time = self.end_time - self.start_time
        print(f'[{self.name}] - Result: {self.result}')
        print(f'[{self.name}] - Total time: {self.total_time:.6f}s')

    @abc.abstractmethod
    def solve(self):
        pass
