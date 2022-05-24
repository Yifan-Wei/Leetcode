from typing import List
from C0000_ClassTree import *

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        last_node = None
        res = None
        def inorder(node):
            nonlocal last_node, res
            if node is None:
                return
            if res:
                return
            # 中序遍历
            inorder(node.left)
            if last_node == p:
                res = node
            last_node = node
            inorder(node.right)
        inorder(root)
        return res.val

if __name__ == '__main__':
    s = Solution()
    # tree = generateTreeNode(None, [2,1,null,null,3])
    tree = generateTreeNode(None, [5,3,2,1,null,null,null,4,null,null,6,null,null])
    result = s.inorderSuccessor(tree, tree)
    print(result)
