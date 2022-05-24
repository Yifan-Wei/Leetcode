class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """0=<word.length<=500"""
        # 本质只有三种操作, a.A增加字符, b.B增加字符, c.A修改字符
        # 从字符horse到字符ros的编辑距离=min(a+1, b+1, c+1)

        # 最长不连续共有子串
        n, m = len(word1), len(word2)
        # -----------------------------------------------
        if m*n==0: return m+n # 空串快速处理
        # -----------------------------------------------
        # A前i个字符和B前j个字符之间的最小操作数目
        dp = [[0]*(m+1) for _ in range(n+1)]
        # -----------------------------------------------
        for ii in range(n+1):
            dp[ii][0] = ii
        for jj in range(m+1):
            dp[0][jj] = jj
        # -----------------------------------------------
        # 以 HOR 和 RO为例
        # a. dp["HO"]["RO"] + 1
        # b. dp["HOR"]["R"] + 1
        # c. dp["HO"]["R"]+1, 任意替换"R"<->"O"
        # dp[i][j] = 1+ min(dp[i-1][j], dp[i][j-1], dp[i-1]][j-1])
        # -----------------------------------------------
        for ii in range(1, n+1):
            for jj in range(1, m+1):
                left = dp[ii-1][jj]+1
                down = dp[ii][jj-1]+1
                left_down = dp[ii-1][jj-1]
                # 如果不相等要替换, 相等则无需替换
                if word1[ii-1] != word2[jj-1]:
                    left_down += 1
                dp[ii][jj]=min(left, down, left_down)

        return dp[n][m]

    def minDistance_Official(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        # 有一个字符串为空串
        if n * m == 0:
            return n + m

        # DP 数组
        D = [[0] * (m + 1) for _ in range(n + 1)]

        # 边界状态初始化
        for i in range(n + 1):
            D[i][0] = i
        for j in range(m + 1):
            D[0][j] = j

        # 计算所有 DP 值
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = D[i - 1][j] + 1
                down = D[i][j - 1] + 1
                left_down = D[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                D[i][j] = min(left, down, left_down)

        return D[n][m]

if __name__ == "__main__":
    s = Solution()
    result = s.minDistance_Official(word1="pneumonoultramicroscopicsilicovolcanoconiosis", word2="ultramicroscopically")
    print(result)
