from typing import List
from C0000_ClassTree import *

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [(root, 0)]
        last_depth = -1
        while queue:
            node, depth = queue.pop(0)
            if not node:
                continue
            if depth > last_depth:
                res = node.val
            last_depth = depth
            queue.append((node.left, depth+1))
            queue.append((node.right, depth+1))
        return res


if __name__ == '__main__':
    s = Solution()
    result = s.a()
    print(result)
