class Solution:
    from typing import List
    def numDecodings(self, s: str) -> int:
        base = ord("A")
        reflect_dict = {}
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        print(dp)
        # -------------------------
        # if n == 1: return 1
        # -------------------------
        for ii in range(1,27):
            reflect_dict[str(ii)] = chr(ii+base-1)
        # -------------------------

        for ii in range(1,n+1):
            # print(ii,"-------------------")
            if ii>=1:
                tmp = s[ii-1:ii]
                # print(tmp)
                if tmp in reflect_dict.keys():
                    dp[ii] = dp[ii] + dp[ii - 1]
            if ii>=2:
                tmp = s[ii-2:ii]
                # print(tmp)
                if tmp in reflect_dict.keys():
                    dp[ii] = dp[ii] + dp[ii - 2]
        # print(dp)
        return dp[n]

if __name__ == '__main__':
    s = Solution()
    result = s.numDecodings("0")
    print(result)
