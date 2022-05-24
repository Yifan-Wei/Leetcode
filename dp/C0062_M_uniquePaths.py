class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m行 n列
        dp = [[0] * m for _ in range(n)]

        # -------------
        # 初始化边界条件
        dp[0][0] = 1
        for ii in range(m):
            dp[0][ii] = 1
        for jj in range(n):
            dp[jj][0] = 1
        # -------------
        for ii in range(1,m):
            for jj in range(1,n):
                dp[jj][ii] = dp[jj][ii-1] + dp[jj-1][ii]
        print(dp)
        return dp[n-1][m-1]


if __name__ == "__main__":
    s = Solution()
    result = s.uniquePaths(m=3, n=3)
    print(result)