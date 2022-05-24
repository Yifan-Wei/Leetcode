from typing import List
from C0000_ClassListNode import *

class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 0<=headA.length<=3*10**4
        # 进阶: 时间复杂度O(N), 空间复杂度O(1)
        # ----------------------------------------
        if headA is None or headB is None:
            return None
        # ----------------------------------------
        pA = headA
        pB = headB
        while True:
            # ----------------------------
            if pA is None and pB is None:
                return None
            if pA == pB:
                return pA
            # ----------------------------
            if pA is None:
                pA = headB
            else:
                pA = pA.next
            # ----------------------------
            if pB is None:
                pB = headA
            else:
                pB = pB.next


    def HASH_getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 0<=headA.length<=3*10**4
        # 时间复杂度O(N), 空间复杂度O(N)

        # ----------------------------------------
        if headA is None or headB is None:
            return None
        # ----------------------------------------
        visited = []
        up = headA
        down = headB
        while up is not None:
            visited.append(up)
            up = up.next
        while down is not None:
            if down in visited:
                return down
            down = down.next
        if up is None and down is None:
            return None



if __name__ == '__main__':
    s = Solution()
    list_node_1 = generateListNode([4,1])
    list_node_2 = generateListNode([5,0,1])
    # list_node_3 = generateListNode([8,4,5])
    # list_node_1.find_tail().next = list_node_3
    # list_node_2.find_tail().next = list_node_3
    list_node_1.print_to_the_end()
    list_node_2.print_to_the_end()
    result = s.getIntersectionNode(list_node_1,list_node_2)
    print_self(result)
