class Solution:
    def climbStairs(self, n: int) -> int:
        """1<=n<=45"""
        if n ==1: return 1
        dp = [0]*n
        dp[0] = 1
        dp[1] = 2
        for ii in range(2,n):
            dp[ii] = dp[ii-1] + dp[ii-2]
        # print(dp)
        return dp[n-1]

if __name__ == "__main__":
    s = Solution()
    result = s.climbStairs(1)
    print(result)
