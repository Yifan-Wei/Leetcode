from C0000_ClassTree import *

class Solution:
    from typing import List
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def combine(link1, link2):
            if link1 is None:
                return link2
            else:
                tmp = link1
                # print(tmp.val)
                while tmp.right is not None:
                    tmp = tmp.right
                tmp.right = link2
                return link1

        def iter_flatten(node):
            if node is None:
                return None
            # print("iter with", node.val)
            left_node = node.left
            right_node = node.right
            node.left = None
            node.right = combine(iter_flatten(left_node), iter_flatten(right_node))
            return node
        iter_flatten(root)

        handle = root
        res = []
        while handle is not None:
            res.append(handle.val)
            handle = handle.right
        print(res)

if __name__ == '__main__':
    s = Solution()
    # tree = generateTreeNode(None, [1,2,3,null,null,4,null,null,5,null,6,null,null])
    tree = generateTreeNode(None,[0])
    result = s.flatten(tree)
    print(result)
