from typing import List

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.window_size = size
        self.total = 0
        self.queue = []

    def next(self, val: int) -> float:
        n = len(self.queue)
        if n>= self.window_size:
            pop_val = self.queue.pop(0)
            self.total -= pop_val
        self.queue.append(val)
        self.total += val

        return self.total/len(self.queue)


if __name__ == '__main__':
    s = MovingAverage()
    result = s.a()
    print(result)
