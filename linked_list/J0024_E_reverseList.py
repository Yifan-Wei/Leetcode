from typing import List
from C0000_ClassListNode import *

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 空表无需反转--------------
        if head is None:
            return None
        # -------------------------
        dummy = ListNode()
        tail = head
        while tail.next is not None:
            tail = tail.next
        new_tail = None
        while head != tail:
            move_to_end = head
            head = head.next
            move_to_end.next = new_tail
            new_tail = move_to_end
        tail.next = new_tail
        dummy.next = tail
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    linked_list = generateListNode([1, 2, 3, 4, 5])
    result = s.reverseList(linked_list)
    print_self(result)
