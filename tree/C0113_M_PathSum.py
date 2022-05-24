from C0000_ClassTree import *

class Solution:
    from typing import Optional
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = []
        def dfs(node, tmp_sum, res) -> None:
            if node is None:
                return
            # print(node.val, tmp_sum, res)
            tmp_sum.append(node.val)
            if node.left is None and node.right is None and sum(tmp_sum) == targetSum:
                res.append(tmp_sum.copy())
            dfs(node.left, tmp_sum, res)
            dfs(node.right, tmp_sum, res)
            tmp_sum.pop()
            return
        dfs(root, [], res)
        return res

if __name__ == '__main__':
    s = Solution()
    tree = generateTreeNode(None, [5,4,11,7,null,null,2,null,null,null,8,13,null,null,4,5,null,null,1,null,null])
    # tree = generateTreeNode(None, [1,2,null,null])
    # tree = None
    result = s.hasPathSum(tree,22)
    print(result)
