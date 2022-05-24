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
    from typing import List
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # ------------------------
        if root is None: return []
        # ------------------------
        # BFS使用队列结构进行操作
        res = [[]]
        queue = [(0, root)]
        while queue:
            depth, node = queue.pop(0)
            if node is None:
                continue
            while len(res)<depth+1:
                res.append([])
            res[depth].append(node.val)
            queue.append((depth+1, node.left))
            queue.append((depth+1, node.right))
        for ii in range(len(res)):
            if ii%2:
                res[ii] = res[ii][::-1]
        return res

if __name__ == '__main__':
    s = Solution()
    null = None
    tree = generateTreeNode(None,[1,2,4,null,null,5,null,null,3,6,null,null,7])
    # tree = generateTreeNode(None,[1])
    # tree = None
    result = s.zigzagLevelOrder(tree)
    print(result)
