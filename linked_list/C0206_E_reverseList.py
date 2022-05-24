from typing import List
from C0000_ClassListNode import *

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None: return None
        tail = head
        while tail.next:
            tail = tail.next
        print(head.val,tail.val)
        new_tail = None
        new_head = head
        while new_head != tail:
            print(new_head.val)
            # 装头
            tmp = new_head
            new_head = new_head.next
            # 接尾巴
            tmp.next = new_tail
            new_tail = tmp
        new_head.next = new_tail

        return new_head


if __name__ == '__main__':
    s = Solution()
    linked_list = generateListNode([1,2,3,4,5])
    result = s.reverseList(linked_list)
    print_self(result)
