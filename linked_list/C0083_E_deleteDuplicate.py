# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def print_self(self):
        tmp = self
        res = []
        while tmp.next is not None:
            res.append(tmp.val)
            tmp=tmp.next
        print(res)

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        res_node = ListNode()
        res_node.next = head
        last_val = -2**31
        handle = res_node
        while True:
            this_node = handle.next
            if this_node is None:
                break
            if this_node.val == last_val:
                handle.next = this_node.next
            else:
                last_val = this_node.val
                handle = this_node
        return res_node.next

if __name__ == "__main__":
    s = Solution()
    node = ListNode(0,ListNode(0,ListNode(1,ListNode(1,ListNode(2,ListNode(3,None))))))
    node.print_self()
    result = s.deleteDuplicates(node)
    result.print_self()
    # print(result)