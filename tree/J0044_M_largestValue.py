from typing import List
from C0000_ClassTree import *

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        # -空节点跳出
        if root is None: return []
        # ----------------------------------------------
        queue, res = [root], []
        depth = 0
        while queue:
            n = len(queue)
            for ii in range(n):
                node = queue.pop(0)
                if node is None:
                    continue
                if depth<len(res):
                    res[depth] = max(res[depth], node.val)
                else:
                    res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            depth += 1
        return res

if __name__ == '__main__':
    s = Solution()
    tree = generateTreeNode(None, [1,2,4,null,null,5,null,null,3,null,null])
    result = s.largestValues(tree)
    print(result)
