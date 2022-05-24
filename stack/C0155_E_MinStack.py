from typing import List


class MinStack:

    def __init__(self):
        self.stack = []
        self.ministack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.ministack:
            self.ministack.append(val)
        else:
            if val <= self.ministack[-1]:
                self.ministack.append(val)
        # print(self.ministack)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.ministack[-1]:
                self.ministack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        return self.ministack[-1]

if __name__ == '__main__':
    obj = MinStack()
    obj.push(val=3)
    obj.push(val=2)
    obj.push(val=1)
    obj.push(val=2)
    obj.push(val=1)
    obj.pop()
    print(obj.getMin())
    # obj.pop()
    # param = obj.top()
    # print(param)
    # param = obj.getMin()
    # print(param)
