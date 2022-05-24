from typing import List
from C0000_ClassTree import *

class CBTInserter:
    # 最初给定的树是完全二叉树，且包含 1 到 1000 个节点。
    # 每个测试用例最多调用 CBTInserter.insert  操作 10000 次
    def __init__(self, root: TreeNode):
        self.total_node = 0
        self.depth = 0
        self.last_p = 0
        self.tree = root
        self.queue = []
        self.init_queue()

    def init_queue(self):
        init_queue = [self.get_root()]
        while init_queue:
            node = init_queue.pop(0)
            if node is None:
                continue
            # 正式入队(BFS 层序)
            self.queue.append(node)
            self.total_node += 1
            if self.total_node > 2**self.depth-1:
                self.depth += 1
            print(node.val, self.total_node, self.depth)
            # 处理入队
            init_queue.append(node.left)
            init_queue.append(node.right)

    def insert(self, v: int) -> int:
        new_node = TreeNode(v)
        if self.queue:
            father_node = self.queue[(self.total_node-1) // 2]
            print("TOTAL = {0}, FATHER = {1}".format(self.total_node, father_node.val))
            if (self.total_node-1) % 2:
                print("RIGHT")
                father_node.right = new_node
            else:
                print("LEFT")
                father_node.left = new_node
        else:
            father_node = None
            print("TOTAL = {0}, FATHER is None".format(self.total_node))
            self.tree = new_node
        self.queue.append(new_node)
        # ----renew------
        self.total_node += 1
        if self.total_node > 2 ** self.depth - 1:
            self.depth += 1
        # ---------------
        return father_node

    def get_root(self) -> TreeNode:
        return self.tree

if __name__ == '__main__':
    # tree = generateTreeNode(None,[1,2,4,null,null,5,null,null,3,6,null,null])
    tree = generateTreeNode(None, [1])
    s = CBTInserter(tree)
    # print(s.insert(1))
    print(s.insert(2))
    # print(s.insert(3))
    # (s.insert(4))
    # print(s.insert(5))
    #print(s.insert(6))
    # print(s.insert(7))
    # print(s.insert(8))
    # print(s.insert(9))
    # print(s.insert(10))
    # print(s.insert(11))
    tree = s.get_root()

