class Solution:
    from typing import List
    def dp_jump(self, nums: List[int]) -> int:
        """
        :param nums:
        :return:
        dp[i]代表到达该位置的最小次数
        dp[i] = min(for x in range(i) min(dp[i-x]))
        dp[0]=0
        """
        # 超时
        n = len(nums)
        dp = [2**31-1] * n
        dp[0]=0
        best_start_index = 0
        for ii in range(1, n):
            while ii > best_start_index + nums[best_start_index]:
                best_start_index += 1
            dp[ii] = dp[best_start_index]+1
        return dp[n-1]

    def greed_jump(self,nums):
        if len(nums)<=1:
            return 0
        currJumpMax = 0     # 以当前跳跃步数，能到的最远位置，比如: jump=1跳一次时，最远能到下标currJumpMax=2
        currPosMax = 0      # 当前位置能到的最远位置
        jump = 0
        i = 0
        while i< len(nums)-1:
            currPosMax = max(currPosMax, i+nums[i])
            if i == currJumpMax:
                jump += 1
                currJumpMax = currPosMax
            i += 1
        return jump

if __name__ == "__main__":
    s = Solution()
    result = s.dp_jump([2,2,3,6,1,1,1,1,1,1])
    print(result)