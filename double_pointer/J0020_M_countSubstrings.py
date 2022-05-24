from typing import List


class Solution:
    """1 <= s.length <= 1000"""
    def BFS_DP_countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        # dp[ii-1][jj+1] is palindrome if s[ii-1]==s[jj+1]
        # if s[ii] == s[jj] and (ii + 1 > jj - 1 or dp[ii + 1][jj - 1] == 1):
        #     dp[ii][jj] = 1
        queue = []
        for ii in range(n):
            queue.append([ii,ii])
        # BFS
        while queue:
            ii, jj = queue.pop(0)
            # -异常跳出--------------------------
            if ii<0 or ii>=n or jj<0 or jj>=n or ii>jj:
                continue
            # ----------------------------------
            # print(ii, jj)
            # 两端相等, 长度2以内的都为回文
            if s[ii] == s[jj]:
                if jj-ii<2 or dp[ii + 1][jj - 1] == 1:
                    dp[ii][jj] = 1
            queue.append([ii, jj + 1])
        # for each in dp:
        #     print(each)
        return sum(sum(dp[ii]) for ii in range(n))

    def countSubstrings(self, s: str) -> int:
        # 中心扩展
        n = len(s)
        res = 0
        for ii in range(2*n-1):
            left = ii // 2
            right = ii // 2 + ii % 2
            while (left >= 0 and right < n and s[left] == s[right]):
                left -= 1
                right += 1
                res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    result = s.countSubstrings("abcdefg")
    print(result)
