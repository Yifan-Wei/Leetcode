from typing import List
from C0000_ClassTree import *

class Codec:
    # 树中节点数范围是[0, 10**4]
    # 0 <= Node.val <= 104
    # 题目数据保证输入的树是一棵二叉搜索树。
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        res = ""

        def mid_order(node):
            if node is None:
                return "N"
            left = mid_order(node.left)
            right = mid_order(node.right)
            # ----------------------------
            tmp = ""
            mid = str(node.val)
            tmp += (mid + "#")
            tmp += (left + "#")
            tmp += (right + "#")
            # --------------------------
            return tmp
        res = mid_order(root)
        return res

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        data_list = data.split("#")
        for ii in range(len(data_list)-1, -1, -1):
            if not data_list[ii]:
                data_list.pop(ii)
            else:
                if data_list[ii]=="N":
                    data_list[ii] = None
                else:
                    data_list[ii] = int(data_list[ii])
        print(data_list)

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
        return generateTreeNode(None, data_list)

if __name__ == '__main__':
    ser = Codec()
    deser = Codec()
    root = generateTreeNode(None, [30,20,10,null,null,null,50,40,null,null,60,null,null])
    tree = ser.serialize(root)
    print(tree)
    ans = deser.deserialize(tree)
    print(ans)
    tree = ser.serialize(ans)
    print(tree)

