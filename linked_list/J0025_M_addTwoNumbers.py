from typing import List
from C0000_ClassListNode import *

class Solution:
    # 进阶：如果输入链表不能修改该如何处理？换句话说，不能对列表中的节点进行翻转。
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def generateListNode(nums):
            res = ListNode()
            last = res
            for each in nums:
                tmp = ListNode(each, None)
                last.next = tmp
                last = tmp
            return res.next

        def fill_queue(l:ListNode, q:List) -> None:
            handle = l
            while handle is not None:
                q.insert(0, handle.val)
                handle = handle.next
        q1 = []
        q2 = []
        fill_queue(l1, q1)
        fill_queue(l2, q2)
        max_len = max(len(q1),len(q2))
        res = [0] * (max_len + 1)
        last = 0
        for ii in range(max_len):
            if ii > len(q1)-1:
                add1 = 0
            else:
                add1 = q1[ii]
            if ii > len(q2)-1:
                add2 = 0
            else:
                add2 = q2[ii]
            total = add1 + add2 + last
            res[ii] = total % 10
            last = total // 10
        if last:
            res[ii+1] = last
        else:
            res.pop()
        res = res[::-1]
        return generateListNode(res)


    def REVERSE_addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 链表的长度范围为[1, 100]
        # 0 <= node.val <= 9
        # 输入数据保证链表代表的数字无前导0
        def reverseList(head: ListNode) -> ListNode:
            # 空表无需反转--------------
            if head is None:
                return None
            # -------------------------
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
            return tail

        p1 = reverseList(l1)
        p2 = reverseList(l2)
        last = 0
        last_node = ListNode()
        head = last_node
        p1.print_to_the_end()
        p2.print_to_the_end()
        while p1 or p2:
            # ------------------------
            if p1:
                add1 = p1.val
                p1 = p1.next
            else:
                add1 = 0
            # ------------------------
            if p2:
                add2 = p2.val
                p2 = p2.next
            else:
                add2 = 0
            # ------------------------
            print(add1, add2, last)
            sum = add1 + add2 + last
            last = sum // 10
            last_node.next = ListNode(sum % 10)
            last_node = last_node.next
        if last>0:
            last_node.next = ListNode(last)
        return reverseList(head.next)
if __name__ == '__main__':
    s = Solution()
    l1 = generateListNode([7,2,4,3])
    l2 = generateListNode([5,6,4])
    result = s.addTwoNumbers(l1,l2)
    print_self(result)
