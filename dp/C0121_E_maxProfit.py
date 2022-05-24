class Solution:
    from typing import List
    def maxProfit(self, prices: List[int]) -> int:
        """prices.length<=10**5"""
        # 找到每个位置右侧最大的数, 单调栈？
        # 单调栈的作用是: 用O(n)的时间得知所有位置两边第一个比他大(或小)的数的位置。
        right_max = -1
        n = len(prices)
        dp = [0] * n
        for ii in range(n-1,-1,-1):
            if prices[ii] < right_max:
                dp[ii] = right_max
            else:
                right_max = prices[ii]
                dp[ii] = 0
        # print(dp)
        res = 0
        for ii in range(n):
            res = max(res, dp[ii]-prices[ii])
        return res

if __name__ == '__main__':
    s = Solution()
    result = s.maxProfit([1,7,5,3,2,4,1,3])
    print(result)
