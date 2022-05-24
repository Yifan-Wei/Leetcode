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
    from typing import List
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res


if __name__ == '__main__':
    s = Solution()
    null = None
    root = None
    tree = generateTreeNode(None, [5,4,null,null,6,3,null,null,7])
    # print(node)
    result = s.inorderTraversal(tree)
    print(result)
