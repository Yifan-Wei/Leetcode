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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def iterSymmetric(mirror_left, mirror_right):
            if mirror_left is None and mirror_right is None:
                print("Double None")
                return True
            if mirror_left is None or mirror_right is None:
                print("Some None")
                return False
            print(mirror_left.val, mirror_right.val)
            if mirror_left.val != mirror_right.val:
                print("Wrong Val")
                return False
            outSymmetric =  iterSymmetric(mirror_left.left, mirror_right.right)
            innerSymmetric = iterSymmetric(mirror_left.right, mirror_right.left)
            return (outSymmetric and innerSymmetric)

        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is None or root.right is None:
            return False
        return iterSymmetric(root.left, root.right)

if __name__ == '__main__':
    s = Solution()
    null = None
    # tree = generateTreeNode(None, [1,2,3,null,null,4,null,null,2,4,null,null,3,null,null])
    tree = generateTreeNode(None, [1,2,null,3,null,null,2,null,3,null,null])
    result = s.isSymmetric(tree)
    print(result)
