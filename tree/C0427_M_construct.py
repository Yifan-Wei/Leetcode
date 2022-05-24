
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    from typing import List
    def construct(self, grid: List[List[int]]) -> 'Node':

        # -----------------------------------------
        def is_leaf(mat):
            dim = len(mat)
            if dim<=1: return True, mat[0][0]
            same_val = mat[0][0]
            for ii in range(dim):
                for jj in range(dim):
                    if mat[ii][jj] != same_val:
                        return False, same_val
            return True, same_val

        def generateFTree(root, mat):
            n = len(mat)
            bl_mat_leaf, val = is_leaf(mat)
            # print(bl_mat_leaf, val)
            if bl_mat_leaf:
                root = Node(val, bl_mat_leaf, None, None, None, None)
            else:
                half = n//2
                # TopLeft:
                topLeft = [mat[ii][0:half] for ii in range(0, half)]
                topLeftNode = generateFTree(None, topLeft)
                # print(topLeft)
                # TopRight:
                topRight = [mat[ii][half:n] for ii in range(0, half)]
                topRightNode = generateFTree(None, topRight)
                # print(topRight)
                # LeftBottom:
                bottomLeft = [mat[ii][0:half] for ii in range(half, n)]
                bottomLeftNode = generateFTree(None, bottomLeft)
                # print(bottomLeft)
                # RightBottom:
                bottomRight = [mat[ii][half:n] for ii in range(half, n)]
                bottomRightNode = generateFTree(None, bottomRight)
                # print(bottomRight)
                # 非叶子节点的val无所谓
                root = Node(val, bl_mat_leaf, topLeftNode, topRightNode, bottomLeftNode, bottomRightNode)
            return root

        # ------------------------------------------
        return generateFTree(None, grid)


if __name__ == '__main__':
    s = Solution()
    # matrix = [[1,1,1,1,0,0,0,0],
    #           [1,1,1,1,0,0,0,0],
    #           [1,1,1,1,1,1,1,1],
    #           [1,1,1,1,1,1,1,1],
    #           [1,1,1,1,0,0,0,0],
    #           [1,1,1,1,0,0,0,0],
    #           [1,1,1,1,0,0,0,0],
    #           [1,1,1,1,0,0,0,0]]
    matrix = [[0]]
    result = s.construct(matrix)
    print(result)
