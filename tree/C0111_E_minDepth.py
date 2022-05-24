from C0000_ClassTree import *

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # ------------------------
        if root is None: return 0
        # ------------------------
        # BFS使用队列结构进行操作
        queue = [(1, root)]
        while queue:
            depth, node = queue.pop(0)
            if node is None: continue
            if node.left is None and node.right is None:
                return depth
            queue.append((depth + 1, node.left))
            queue.append((depth + 1, node.right))

if __name__ == '__main__':
    s = Solution()
    tree = generateTreeNode(None,[2,null,3,null,4,null,5,null,6])
    result = s.minDepth(tree)
    print(result)
