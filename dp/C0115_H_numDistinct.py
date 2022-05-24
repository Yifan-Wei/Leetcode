class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s_len, t_len = len(s), len(t)
        # dp代表s中前ii个字符可以由t中前jj个字符组成最多个数
        dp = [[0] * (s_len+1) for _ in range(t_len+1)]
        # 当ii=0时, 空字符串不存在空集以外的子集
        for ii in range(1, t_len+1):
            dp[ii][0] = 0
        # 当jj=0时, 空集是所有字符串子集, 且只有1种组成方法
        for jj in range(s_len+1):
            dp[0][jj] = 1
        # print(dp)
        for ii in range(1, t_len + 1):
            for jj in range(1, s_len + 1):
                if t[ii-1] == s[jj-1]:
                    # 当待匹配串延长时, 如延长的字符与匹配字符相同, 可以不动这个字符(前面的排列组合)和无视这个字符(删掉这个字符前面仍然符合)
                    dp[ii][jj] = dp[ii-1][jj-1] + dp[ii][jj-1]
                else:
                    # 加入不相同字符时, 只能选择删除这个不相同字符
                    dp[ii][jj] = dp[ii][jj-1]
        #for each in dp:
            #print(each)
        return dp[t_len][s_len]

if __name__ == '__main__':
    s = Solution()
    result = s.numDistinct(s="babgbag", t="bag")
    print(result)
