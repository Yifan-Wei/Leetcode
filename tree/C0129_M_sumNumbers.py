from C0000_ClassTree import *

class Solution:
    from typing import List
    def sumNumbers(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, s_list):
            nonlocal res
            if node is None:
                return
            # print(node.val, s_list)
            s_list.append(node.val)
            if node.left is None and node.right is None:
                multi = 1
                for each in s_list[::-1]:
                    res += each * multi
                    multi *= 10
                # print("Leaf", res)
                pass
            if node.left:
                dfs(node.left, s_list)
            if node.right:
                dfs(node.right, s_list)
            s_list.pop()
        dfs(root, [])
        return res


if __name__ == '__main__':
    s = Solution()
    tree = generateTreeNode(None, [1,2,null,null,3])
    # tree = generateTreeNode(None, [4,9,5,null,null,1,null,null,0,null,null])
    result = s.sumNumbers(tree)
    print(result)
