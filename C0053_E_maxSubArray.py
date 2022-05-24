class Solution:
    from typing import List
    def maxSubArray(self, nums: List[int]) -> int:
        """
        进来的如果是正数肯定无脑要, 如果是负数就分为要和不要两种情况
        dp[ii] = max(dp[ii-1]+nums[ii], nums[ii])
        :param nums:
        :return:
        """
        res = -2**31
        combo_res = -2**31
        for ii in range(len(nums)):
            res = max(res, combo_res)
            res = max(res, nums[ii])
            combo_res += nums[ii]
            if nums[ii] > combo_res:
                combo_res = nums[ii]
        return max(res, combo_res)

if __name__ == "__main__":
    s = Solution()
    result = s.maxSubArray([-2,-1,-5])
    print(result)