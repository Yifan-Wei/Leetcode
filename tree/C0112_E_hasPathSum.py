from C0000_ClassTree import *

class Solution:
    from typing import Optional
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, sum) -> bool:
            if node is None:
                return False
            # print(node.val, sum)
            tmp_sum = sum+node.val
            if node.left is None and node.right is None and  tmp_sum == targetSum:
                return True
            else:
                return dfs(node.left, tmp_sum) or dfs(node.right, tmp_sum)
        return dfs(root,0)

if __name__ == '__main__':
    s = Solution()
    # tree = generateTreeNode(None, [5,4,11,7,null,null,2,null,null,null,8,13,null,null,4,null,1,null,null])
    tree = generateTreeNode(None, [1,2,null,null])
    # tree = None
    result = s.hasPathSum(tree,3)
    print(result)
