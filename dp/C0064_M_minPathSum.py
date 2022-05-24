class Solution:
    from typing import List
    def minPathSum(self, grid: List[List[int]]) -> int:
        # m行 n列
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * m for _ in range(n)]
        # -------------
        # 初始化边界条件
        dp[0][0] = grid[0][0]
        # -------------
        for ii in range(0, m):
            for jj in range(0, n):
                if ii-1>=0 and jj-1>=0:
                    dp[jj][ii] = min(dp[jj][ii-1], dp[jj-1][ii]) + grid[jj][ii]
                elif ii-1>=0 and jj-1<0:
                    dp[jj][ii] = dp[jj][ii-1] + grid[jj][ii]
                elif ii-1<0 and jj-1>=0:
                    dp[jj][ii] = dp[jj-1][ii] + grid[jj][ii]
        print(dp)
        return dp[n-1][m-1]


if __name__ == "__main__":
    s = Solution()
    result = s.minPathSum([[1,2,3],[4,5,6]])
    print(result)