from typing import List
from C0000_ClassTree import *

class Codec:
    # 树中结点数在范围[0, 10**4]内
    # -1000 <= Node.val <= 1000
    def __init__(self):
        self.midorder_list = []

    def preorder(self, node):
        if node is None:
            self.midorder_list.append(None)
        else:
            self.midorder_list.append(node.val)
        # LEFT
        if node.left:
            self.preorder(node.left)
        else:
            self.midorder_list.append(None)
        # RIGHT
        if node.right:
            self.preorder(node.right)
        else:
            self.midorder_list.append(None)

    def serialize(self, root):
        if root is None:
            return ""
        self.preorder(root)
        preorder_string = ""
        for ii, each in enumerate(self.midorder_list):
            if ii:
                preorder_string += "#"+str(each)
            else:
                preorder_string = str(each)
        return preorder_string

    def generateOrderTree(self, node, order):
        if len(order) == 0:
            return node
        jval = order.pop(0)
        if jval != "None":
            new_node = TreeNode(int(jval))
            new_node.left = self.generateOrderTree(node, order)
            new_node.right = self.generateOrderTree(node, order)
            return new_node
        return None

    def deserialize(self, data):
        if not data: return None
        order = data.split("#")
        return self.generateOrderTree(None, order)

if __name__ == '__main__':
    # tree = generateTreeNode(None,[1,2,null,null,3,4,null,null,5])
    # tree = generateTreeNode(None, [1,1,2,null,null,3,null,null,2,3,null,null,4])
    tree = None
    ser = Codec()
    deser = Codec()
    # print(ser.serialize(tree))
    ans = deser.deserialize(ser.serialize(tree))
