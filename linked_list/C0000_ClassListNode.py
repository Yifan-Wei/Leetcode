from typing import List

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_to_the_end(self, iter_max=20):
        list = []
        tmp = self
        iter = 0
        while tmp is not None and iter<=iter_max:
            iter += 1
            list.append(tmp.val)
            tmp = tmp.next
        print(list)

    def find_tail(self):
        tmp = self
        while tmp.next is not None:
            tmp = tmp.next
        return tmp

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_to_the_end(self, iter_max=20):
        list = []
        tmp = self
        iter = 0
        while tmp is not None and iter<=iter_max:
            iter += 1
            list.append(tmp.val)
            tmp = tmp.next
        print(list)

    def find_tail(self):
        tmp = self
        while tmp.next is not None:
            tmp = tmp.next
        return tmp

def print_self(object):
    if object is None:
        print(object)
        return
    object.print_to_the_end()

def generateListNode(nums):
    if nums is None or len(nums)<=0:
        return None
    res = ListNode()
    last = res
    for each in nums:
        tmp = ListNode(each, None)
        last.next = tmp
        last = tmp
    return res.next

def generateNode(nums):
    if nums is None or len(nums)<=0:
        return None
    res = Node()
    last = res
    for each in nums:
        tmp = Node(each, None)
        last.next = tmp
        last = tmp
    return res.next
