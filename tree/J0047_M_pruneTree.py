from typing import List
from C0000_ClassTree import *

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        dummy_root = TreeNode(0)
        dummy_root.left = root

        def deleteTree(father, node, left):
            if node is None:
                return
            if node.left:
                deleteTree(node, node.left, True)
            if node.right:
                deleteTree(node, node.right, False)
            # 如果删除完成后没有子树了
            if not node.left and not node.right and node.val == 0:
                if left:
                    father.left = None
                else:
                    father.right = None

        deleteTree(dummy_root, root, True)

        return dummy_root.left

if __name__ == '__main__':
    s = Solution()
    tree = generateTreeNode(None,[1,0,0,null,null,0,null,null,1,0,null,null,1])
    result = s.pruneTree(tree)
    print(result)
