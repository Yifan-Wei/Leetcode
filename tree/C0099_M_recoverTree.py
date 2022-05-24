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
    from typing import Optional
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        def mid(node, res):
            if node is not None:
                mid(node.left, res)
                res.append(node)
                mid(node.right, res)
        mid(root, res)

        node1 = None
        node2 = None
        #for ii in range(len(res)):
            #print(res[ii].val)
        for i in range(len(res) - 1):
            if res[i].val > res[i + 1].val and node1 == None:
                node1 = res[i]
                node2 = res[i + 1]
                # print("__", node1.val, node2.val)
            elif res[i].val > res[i + 1].val and node1 != None:
                node2 = res[i + 1]
                # print("__", node2.val)
        node1.val, node2.val = node2.val, node1.val

        #for ii in range(len(res)):
            #print(res[ii].val)



if __name__ == '__main__':
    s = Solution()
    null = None
    tree = generateTreeNode(None, [1,3,null,2, null])
    result = s.recoverTree(tree)
    print(result)
