from typing import List
from C0000_ClassListNode import *

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 1<=链表中节点数目<=30
        # 0<=n<=30
        dummy_node = ListNode()
        dummy_node.next = head

        handle_node = dummy_node
        last_node = dummy_node
        delete_node = head
        ii = -1
        while handle_node.next is not None:
            # 当前处理节点更新
            ii += 1
            handle_node = handle_node.next
            # ------------------------------
            if n==0:
                last_node = delete_node
                delete_node = delete_node.next
            else:
                n -= 1
            # ------------------------------
            # 如果满足条件, 将上一个节点直接接到下一个节点
            if handle_node.next is None:
                last_node.next = delete_node.next
            # print_self(dummy_node.next)
        return dummy_node.next


if __name__ == '__main__':
    s = Solution()
    list_node = generateListNode([1,2,3])
    list_node.print_to_the_end()
    result = s.removeNthFromEnd(list_node, 1)
    print_self(result)
