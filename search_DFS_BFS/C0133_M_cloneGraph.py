from typing import List
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def generateAdjList(neighborsList:List):
    if not len(neighborsList): return None
    NodeList = [Node(val=ii+1) for ii in range(len(neighborsList))]
    # print(neighborsList)
    for ii in range(len(neighborsList)):
        getList = neighborsList[ii] #每个节点的邻接表
        for jj in range(len(getList)):
            getNeighborIndex = getList[jj]-1
            print("contact {0} with {1}".format(NodeList[ii].val, NodeList[getNeighborIndex].val))
            NodeList[ii].neighbors.append(NodeList[getNeighborIndex])
    return NodeList[0]

class Solution:
    def __init__(self):
        self.visited = {}
    """Node<=100"""
    def visitAdjList(self, inNode):
        visited = set()
        # print("--------------------------------------------------")
        def dfs_visit(node, visited):
            if node is None:
                return
            if node in visited:
                # print(node.val, "has been visited")
                return
            visited.add(node)
            # print("visited node.val=", node.val)
            if len(node.neighbors) > 0:
                for each in node.neighbors:
                    # print("visited", node.val, "'s neighbor")
                    dfs_visit(each, visited)
        dfs_visit(inNode, visited)
        return len(visited)

    def cloneGraph_self(self, node):
        total_node = self.visitAdjList(node)
        if total_node == 0: return None
        if total_node == 1: return Node(val=1)
        cloneList = [Node(val=ii+1) for ii in range(total_node)]
        visited = set()
        def dfs_clone(curr_node, visited, cloneList):
            if curr_node is None:
                return
            if curr_node in visited:
                return
            # 找到---------------------------------------
            visited.add(curr_node)
            index_curr = curr_node.val - 1
            # -------------------------------------------
            if len(curr_node.neighbors) > 0:
                for each in curr_node.neighbors:
                    # 建立邻接关系-------------------------------
                    index_neighbor = each.val - 1
                    if cloneList[index_neighbor] not in cloneList[index_curr].neighbors:
                        cloneList[index_curr].neighbors.append(cloneList[index_neighbor])
                    if cloneList[index_curr] not in cloneList[index_neighbor].neighbors:
                        cloneList[index_neighbor].neighbors.append(cloneList[index_curr])
                    # 拜访--------------------------------------
                    dfs_clone(each, visited, cloneList)
            # -------------------------------------------
        dfs_clone(node, visited, cloneList)
        # 无邻居输入
        return cloneList[0]

    def cloneGraph(self, node):
        # HASH存储结构为
        # hash[原节点地址] = 克隆节点地址
        # 空节点拷贝返回空
        if not node:
            return node
        # NODE 已经被访问过, HASH直接回归调用已经生成的节点
        if node in self.visited:
            return self.visited[node]
        # 克隆节点
        clone_node = Node(val=node.val)
        # 置为已经克隆过
        self.visited[node] = clone_node
        # 遍历相邻节点
        if node.neighbors:
            for adj_node in node.neighbors:
                # 加入邻居的同时递归
                clone_node.neighbors.append(self.cloneGraph(adj_node))
            # clone_node.neighbors = [self.cloneGraph(adj_node) for adj_node in node.neighbors]
        return clone_node

if __name__ == '__main__':
    s = Solution()
    inNode = generateAdjList([[2,4],[1,3],[2,4],[1,3]])
    # inNode = generateAdjList([[]])
    result = s.cloneGraph(inNode)
    print(result)
    s.visitAdjList(result)
