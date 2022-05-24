# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_self(self):
        tmp = self
        res = []
        while tmp is not None:
            res.append(tmp.val)
            tmp = tmp.next
        print(res)

def generateListNode(nums):
    res = ListNode()
    last = res
    for each in nums:
        tmp = ListNode(each, None)
        last.next = tmp
        last = tmp
    return res.next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        small_node = ListNode()
        small_node_p = small_node
        large_node = ListNode()
        large_node_p = large_node
        this_node = head
        while this_node is not None:
            tail = this_node.next
            this_node.next = None
            if this_node.val < x:
                small_node_p.next = this_node
                small_node_p = this_node
            else:
                large_node_p.next = this_node
                large_node_p = this_node
            # ITER
            this_node = tail

        small_node_p.next=large_node.next

        return small_node.next

if __name__ == "__main__":
    s = Solution()
    node = generateListNode([7,6,5,4,3,2,1,2,3,4,5,6,7])
    node.print_self()
    result = s.partition(node,4)
    result.print_self()
    # print(result)