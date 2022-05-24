from typing import List
from C0000_ClassMultiLayerListNode import *

class Solution:
    # 节点数目不超过1000
    # 1 <= Node.val <= 10 ^ 5
    def flatten(self, head: 'Node') -> 'Node':

        def flatten_node(node):
            if node is None:
                return None
            next_node = node.next
            if node.child:
                if next_node:
                    child_last = flatten_node(node.child)
                    node.next = node.child
                    node.next.prev = node
                    node.child = None
                    child_last.next = next_node
                    next_node.prev = child_last
                else:
                    child_last = flatten_node(node.child)
                    node.next = node.child
                    node.next.prev = node
                    node.child = None
                    child_last.next = None
                    return child_last
            else:
                if next_node is None:
                    return node
            last_node = flatten_node(next_node)
            return last_node

        flatten_node(head)
        # head.print_to_the_end()
        return head

if __name__ == '__main__':
    s = Solution()
    multi1 = generateListNode([1])
    multi2 = generateListNode([2])
    multi3 = generateListNode([3])
    multi1.child = multi2
    multi2.child = multi3
    result = s.flatten(multi1)
    print(result)
