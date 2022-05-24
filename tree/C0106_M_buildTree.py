# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # print(inorder, postorder)
        if len(inorder)==0:
            return None
        mid = postorder[-1]
        # print(mid)
        for ii in range(len(inorder)):
            if inorder[ii]==mid:
                break
        return TreeNode(mid, self.buildTree(inorder[0:ii],postorder[0:ii]), self.buildTree(inorder[ii + 1:],postorder[ii:-1]))

if __name__ == '__main__':
    s = Solution()
    result = s.buildTree([9,3,15,20,7],
                         [9,15,7,20,3])
    print(result)
