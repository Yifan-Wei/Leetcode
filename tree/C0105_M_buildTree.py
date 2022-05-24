# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder)==0:
            return None
        mid = preorder[0]
        for ii in range(len(inorder)):
            if inorder[ii]==mid:
                break
        return TreeNode(mid, self.buildTree(preorder[1:1+ii], inorder[0:ii]), self.buildTree(preorder[1+ii:], inorder[ii+1:]))

if __name__ == '__main__':
    s = Solution()
    result = s.buildTree(preorder = [3,9,20,15,7],
                         inorder = [9,3,15,20,7])
    print(result)
