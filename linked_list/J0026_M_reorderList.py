from typing import List
from C0000_ClassListNode import *

class Solution:
    # 链表的长度范围为[1, 5 * 10 ** 4]
    # 1 <= node.val <= 1000
    def reorderList(self, head: ListNode) -> None:
        queue = []
        handle = head
        while handle:
            queue.append(handle)
            handle = handle.next
        left = 0
        right = len(queue)-1
        while right - left >= 2:
            queue[right - 1].next = None
            queue[left].next = queue[right]
            queue[right].next = queue[left + 1]
            left += 1
            right -= 1
        print_self(head)


    def ON2_reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reorder(node):
            if node is None:
                return None
            tail = node
            last = None
            while tail.next is not None:
                last = tail
                tail = tail.next
            print(tail.val)
            if last:
                last.next = None
                tail.next = node.next
                node.next = tail
                node.print_to_the_end()
                reorder(tail.next)
            else:
                return
        reorder(head)
        print_self(head)
        #head.print_to_the_end()

if __name__ == '__main__':
    s = Solution()
    linked_list = generateListNode([1])
    result = s.reorderList(linked_list)
    print(result)
