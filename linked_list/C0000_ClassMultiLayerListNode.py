from typing import List
class Node:
    def __init__(self, val=0, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    def find_head(self):
        tmp = self
        while tmp.prev is not None:
            tmp = tmp.prev
        return tmp

    def find_tail(self):
        tmp = self
        while tmp.next is not None:
            tmp = tmp.next
        return tmp

    def print_to_the_end(self, iter_max=100):
        list = []
        tmp = self
        iter = 0
        while tmp is not None and iter<=iter_max:
            iter += 1
            list.append(tmp.val)
            tmp = tmp.next
        print(list)

def print_self(object):
    if object is None:
        print(object)
        return
    object.print_to_the_end()


def generateListNode(nums):
    if nums is None or len(nums)<=0:
        return None
    res = Node()
    flag_first = True
    last = res
    for each in nums:
        tmp = Node(val=each, prev=None, next=None)
        last.next = tmp
        if flag_first:
            flag_first = False
        else:
            tmp.prev = last
        last = tmp
    return res.next
