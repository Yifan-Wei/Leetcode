class Solution:
    """回文字符串的最小分割次数"""
    from typing import List
    def minCut(self, s: str) -> int:
        n = len(s)

        def is_palindrome(input_s):
            if len(input_s)<=1: return True
            return input_s == input_s[::-1]
        dp = [2**31] * (n)
        # dp代表前n个字符的最小分割次数
        for ii in range(n):
            # 正在处理第ii位字符串
            # print("-------",ii,s[ii],"-------")
            if is_palindrome(s[:ii + 1]):
                # print("{0} is palindrome, continue".format(s[:ii + 1]))
                dp[ii] = 0
                continue
            for jj in range(1, ii+1):
                if is_palindrome(s[jj:ii + 1]):
                    # print("{0} is palindrome, try cut in it".format(s[jj:ii + 1]))
                    # print("BEFORE: dp[{2}]={0},dp[{3}]={1}, while ii={2},jj={3}".format(dp[ii],dp[jj-1],ii,jj-1))
                    dp[ii] = min(dp[jj-1]+1, dp[ii])
                    # print("AFTER: dp[{1}]={0} while ii={1}".format(dp[ii], ii))
        return dp[n-1]

if __name__ == '__main__':
    s = Solution()
    # result = s.minCut("abcdefgfedcbb")
    result = s.minCut("aaaabac")
    print(result)
