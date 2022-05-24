from typing import List
from C0000_ClassListNode import *


class Solution:
    def isPalindrome(self, head):
        fast = head
        slow = head
        last = None
        s_cnt = 0
        while fast and fast.next:
            s_cnt += 1
            fast = fast.next.next
            slow = slow.next
            if last:
                last = last.next
            else:
                last = head
        if last:
            last.next = None
        else:
            # print("linked list <=1")
            return True
        if fast:
            sc_head = slow.next
        else:
            sc_head = slow

        def reverse(node):
            tail = node
            while tail.next:
                tail = tail.next
            new_head = node
            new_tail = None
            while new_head != tail:
                tmp = new_head.next
                new_head.next = new_tail
                new_tail = new_head
                new_head = tmp
            tail.next = new_tail
            return new_head

        fst_head = head
        sc_head = reverse(sc_head)
        # print_self(fst_head)
        # print_self(sc_head)
        while fst_head and sc_head:
            if fst_head.val == sc_head.val:
                fst_head = fst_head.next
                sc_head = sc_head.next
            else:
                return False
        return True

    def ONON_isPalindrome(self, head: ListNode) -> bool:
        # 10**5
        res = []
        handle = head
        while handle:
            res.append(handle.val)
            handle = handle.next
        return res==res[::-1]


if __name__ == '__main__':
    s = Solution()
    linked_list = generateListNode([1,2])
    result = s.isPalindrome(linked_list)
    print(result)
