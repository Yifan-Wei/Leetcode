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
            tmp=tmp.next
        print("Node print as :", res)

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        res_node = ListNode(-2**31)
        res_node.next = head
        last_val = -2**31
        handle = res_node
        last_useful_node = res_node
        repeat = -1
        while True:
            this_node = handle.next
            if this_node is None:
                if repeat > 1:
                    last_useful_node.next = this_node
                break
            if this_node.val == last_val:
                handle.next = this_node.next
                repeat += 1
            else:
                if repeat > 1:
                    last_useful_node.next = this_node
                elif repeat == 1:
                    last_useful_node = handle
                repeat = 1
                last_val = this_node.val
            # ITER
            handle = this_node

        return res_node.next

if __name__ == "__main__":
    s = Solution()
    node = ListNode(1, ListNode(1))
    # node = ListNode(0,ListNode(0,ListNode(0,ListNode(1,ListNode(2,ListNode(2,ListNode(3,ListNode(3))))))))
    node.print_self()
    result = s.deleteDuplicates(node)
    if result is not None:
        result.print_self()
    else:
        print("None")
    # print(result)