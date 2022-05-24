from C0000_ClassTree import *

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def is_balanced(node):
            # 空节点和叶子节点都是平衡二叉树---------------------------
            if node is None: return (True, 0)
            if node.left is None and node.right is None:
                print(node.val, "leaf", 1)
                return (True, 1)
            # -------------------------------------------------------
            left_balanced, left_height = is_balanced(node.left)
            right_balanced, right_height = is_balanced(node.right)
            if left_balanced and right_balanced and abs(left_height-right_height)<=1:
                print(node.val, left_height, left_balanced, right_height, right_balanced)
                return True, max(left_height, right_height)+1
            else:
                print(node.val, left_height, left_balanced, right_height, right_balanced)
                return False, max(left_height, right_height)+1
        return is_balanced(root)[0]

if __name__ == '__main__':
    s = Solution()
    # tree = generateTreeNode(None, [3, 9, null, null, 20, 15, null, null, 7, null, null])
    tree=  generateTreeNode(None, [1,2,3,4,null,null,4,null,null,3,null,null,2])
    result = s.isBalanced(tree)
    print(result)
