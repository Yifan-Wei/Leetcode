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
    from typing import Optional
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        WHITE, GREY = 0, 1
        stack = [(WHITE, root)]
        res = []
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
            print_list = []
            for each in stack:
                if each[1] is not None:
                    print_list.append(each[1].val)
                else:
                    print_list.append(None)
            print(print_list)

        # print(res)
        for ii in range(1,len(res)):
            if res[ii]<=res[ii-1]:
                return False
        return True




if __name__ == '__main__':
    s = Solution()
    null = None
    tree = generateTreeNode(None, [2,1,null,null,4,3,null,null,null])
    result = s.isValidBST(tree)
    print(result)
