from typing import List, Optional
from collections import deque
from C0000_ClassListNode import *

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insertTreeNode(self, tree_node):
        if tree_node.val.val <= self.val.val:
            if self.left:
                self.left.insertTreeNode(tree_node)
            else:
                self.left = tree_node
        else:
            if self.right:
                self.right.insertTreeNode(tree_node)
            else:
                self.right = tree_node

    def midorder(self):
        last_node = None
        def midOrderAdd(node):
            nonlocal last_node
            if node is None:
                return
            if node.left:
                midOrderAdd(node.left)
            if last_node:
                last_node.val.next = node.val
            last_node = node
            if node.right:
                midOrderAdd(node.right)
        midOrderAdd(self)
        last_node.val.next = None

class Solution:
    # 链表中节点的数目在范围[0, 5 * 10**4]内
    # -105 <= Node.val <= 105
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-2**31)
        dummy_root = TreeNode(dummy_head)
        link_node = head
        while link_node:
            tree_node = TreeNode(val=link_node)
            dummy_root.insertTreeNode(tree_node)
            link_node = link_node.next
        dummy_root.midorder()
        return dummy_head.next


if __name__ == '__main__':
    s = Solution()
    linked_list = generateListNode([-1,5,3,4,0])
    result = s.sortList(linked_list)
    print_self(result)
