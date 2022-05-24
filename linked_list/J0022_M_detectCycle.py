from typing import List
from C0000_ClassListNode import *

class Solution:

    def FSP_detectCycle(self, head: ListNode) -> ListNode:
        # 快慢指针解决问题, 降低空间复杂度到O(1)
        # 快指针每次走两步, 慢指针每次走一步
        # 情况1, 快指针到底, 说明无环
        # 情况2, 快指针与慢指针相遇, 快指针总路程2i=a+mb, 慢指针总路程i=a+nb
        # i = (m-n) * b (b为环的总长度)
        # 由于任意一个从出口出发, 走a+kb的距离都会抵达环入口, 此时满指针行程为kb, 只需要再走a即可
        # 而同理, 从出发点到入口也只需要走a, 因此在入口出发的和在当前位置出发的指针会重合
        fast, slow = head, head
        while True:
            # 情况1
            if fast is None or fast.next is None:
                return None
            fast, slow = fast.next.next, slow.next
            # 情况2
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast

    def HASH_detectCycle(self, head: ListNode) -> ListNode:
        # HASH表, O(N) * O(N)
        # 给定一个链表，返回链表开始入环的第一个节点。
        visited_node = []
        handle = head
        while handle is not None:
            if handle not in visited_node:
                visited_node.append(handle)
            else:
                return handle
            handle = handle.next
        return None

if __name__ == '__main__':
    s = Solution()
    list_node = generateListNode([3,2,0,-4])
    tail = list_node.find_tail()
    tail.next = list_node.next
    list_node.print_to_the_end(10)
    result = s.FSP_detectCycle(list_node)
    print_self(result)
