class Solution:
    from typing import List
    def canJump(self, nums: List[int]) -> bool:
        """
        :param nums:
        :return:
        (ii, ii + nums[ii])
        """
        if len(nums)<=1:
            return True
        n = len(nums)
        max_jump = 0
        for ii in range(n):
            if ii <= max_jump:
                max_jump = max(max_jump, ii+nums[ii])
                if max_jump>=n-1:
                    return True
        return False

if __name__ == "__main__":
    s = Solution()
    result = s.canJump([3, 2, 1, 0, 4])
    print(result)