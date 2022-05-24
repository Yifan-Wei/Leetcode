class Solution:
    from typing import List
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # m行 n列
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0] * m for _ in range(n)]
        # -------------
        # 初始化边界条件
        if not obstacleGrid[0][0]:
            dp[0][0] = 1
        # -------------
        for ii in range(0, m):
            for jj in range(0, n):
                if not obstacleGrid[jj][ii]:
                    if ii-1>=0 and jj-1>=0:
                        dp[jj][ii] = dp[jj][ii-1] + dp[jj-1][ii]
                    elif ii-1>=0 and jj-1<0:
                        dp[jj][ii] = dp[jj][ii-1]
                    elif ii-1<0 and jj-1>=0:
                        dp[jj][ii] = dp[jj-1][ii]
        print(dp)
        return dp[n-1][m-1]


if __name__ == "__main__":
    s = Solution()
    result = s.uniquePathsWithObstacles([[0,0,0],[0,1,1],[0,0,0]])
    print(result)