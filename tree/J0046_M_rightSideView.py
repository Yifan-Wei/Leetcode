from typing import List
from C0000_ClassTree import *
from collections import deque


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None: return []
        queue = deque()
        res = []
        queue.append((root, 0))
        last_depth = -1
        while queue:
            node, depth = queue.popleft()
            if node is None:
                continue
            if depth == last_depth:
                res[depth] = node.val
            else:
                res.append(node.val)
            last_depth = depth
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))
        return res


if __name__ == '__main__':
    s = Solution()
    # tree = generateTreeNode(None, [1,2,4,null,null,5,null,null,3,null,null])
    tree = generateTreeNode(None, [1, 2, null, 5, null, null, 3, null, 4, null, null])
    result = s.rightSideView(tree)
    print(result)

