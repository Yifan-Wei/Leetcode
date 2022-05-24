from C0000_ClassTree import *

class Solution:
    from typing import Optional
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = -2**31

        def dfs(node):
            nonlocal maxSum
            if node is None:
                return 0
            # 左子树递归
            if node.left:
                max_left = dfs(node.left)
            else:
                max_left = 0
            # 右子树递归
            if node.right:
                max_right = dfs(node.right)
            else:
                max_right = 0
            # 子树内部最大路径和
            inner_max_sum = max_left + node.val + max_right
            # 挑战最大子树路径和
            maxSum = max(inner_max_sum, maxSum)
            # 对外提供最大
            outputmaxSum = node.val + max(0, max_left, max_right)
            # 对外提供
            # print("NODE: {0}, INNER MAX SUM: {1}, OUTPUT: {2}".format(node.val, inner_max_sum, outputmaxSum))
            return outputmaxSum if outputmaxSum>=0 else 0

        dfs(root)
        return maxSum

if __name__ == '__main__':
    s = Solution()
    tree = generateTreeNode(None, [-10,9,null,null,20,15,null,null,7,null,null])
    result = s.maxPathSum(tree)
    print(result)
