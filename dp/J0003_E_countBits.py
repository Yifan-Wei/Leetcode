from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        #  0 <= n <= 10**5
        # 动态规划
        # ii=偶数时 dp[ii] = dp[ii/2] (位运算规则, 向右移位=%2)
        # ii=奇数时 dp[ii] = dp[ii-1]
        res = [0]
        dp = [0] * (n+1)
        for ii in range(1,n+1):
            if (ii % 2):
                dp[ii] = dp[ii-1] +1
            else:
                dp[ii] = dp[(ii>>1)]
            res.append(dp[ii])
        return res


if __name__ == '__main__':
    s = Solution()
    result = s.countBits(1)
    print(result)
