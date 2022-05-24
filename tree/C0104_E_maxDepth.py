# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generateTreeNode(root, val):
    # val值用完了
    if len(val) == 0:
        return root
    # 当前节点是否为空
    if val[0] is not None:
        root = TreeNode(val[0])
        val.pop(0)
        # root.left/root.right默认就是None, 形成递归
        root.left = generateTreeNode(root.left, val)
        root.right = generateTreeNode(root.right, val)
        return root
    else:
        root = None
        val.pop(0)
        return root

class Solution:
    from typing import Optional
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # ------------------------
        if root is None: return 0
        # ------------------------
        max_depth = 0
        # BFS使用队列结构进行操作
        queue = [(1, root)]
        while queue:
            depth, node = queue.pop(0)
            if node is None:
                continue
            max_depth = max(max_depth, depth)
            queue.append((depth+1, node.left))
            queue.append((depth+1, node.right))
        return max_depth


if __name__ == '__main__':
    s = Solution()
    null = None
    tree = generateTreeNode(None,[3,9,null,null,20,15,null,null,7,8,null,null,null])
    result = s.maxDepth(tree)
    print(result)
