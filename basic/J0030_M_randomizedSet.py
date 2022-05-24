from typing import List
from random import randint

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.random_set = set()
        self.total = 0


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.random_set:
            self.random_set.add(val)
            self.total += 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.random_set:
            self.random_set.remove(val)
            self.total -= 1
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        randindex = randint(0,self.total-1)
        return list(self.random_set)[randindex]


if __name__ == '__main__':
    obj = RandomizedSet()
    param_1 = obj.insert(1)
    param_1 = obj.insert(2)
    param_1 = obj.insert(3)
    param_1 = obj.insert(4)
    param_2 = obj.remove(5)
    param_3 = obj.getRandom()
    print(param_1,param_2,param_3)