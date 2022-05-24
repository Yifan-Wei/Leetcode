# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    from typing import List, Optional
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0: return None
        if len(nums)==1: return TreeNode(nums[0], None, None)
        n = len(nums)
        mid = n//2
        # print(nums[0:mid], nums[mid+1:])
        return TreeNode(nums[mid], self.sortedArrayToBST(nums[0:mid]), self.sortedArrayToBST(nums[mid+1:]))




if __name__ == '__main__':
    s = Solution()
    result = s.sortedArrayToBST([-10,-3,0,5,9])
    print(result)
