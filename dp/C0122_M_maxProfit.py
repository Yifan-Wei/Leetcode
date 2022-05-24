class Solution:
    """给你一个整数数组 prices ，其中prices[i] 表示某支股票第 i 天的价格。
    在每一天，你可以决定是否购买和/或出售股票。你在任何时候最多只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。
    返回 你能获得的 最大 利润。
    """
    from typing import List
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n+1)]
        # print(dp)
        dp[0][0] = 0            # 默认第0天不持有股票
        for ii in range(1, n+1):
            # print(ii)
            if ii == 1:
                dp[ii][0] = dp[ii-1][0]
                dp[ii][1] = dp[ii-1][0] - prices[ii-1]
            else:
                # 第ii天不持股票的收益为: ii-1天不持有股票的最大收益, 和ii-1天持有股票但今日卖出持有股票收益 之最大值
                dp[ii][0] = max(dp[ii-1][0], dp[ii-1][1]+prices[ii-1])
                # 第ii天持有股票的收益为: ii-1天持有股票的最大收益, 和ii-1天不持有股票但今日持有股票收益 之最大值
                dp[ii][1] = max(dp[ii-1][1], dp[ii-1][0]-prices[ii-1])
        # print(dp)
        return max(dp[n])

if __name__ == '__main__':
    s = Solution()
    result = s.maxProfit([3,3,5,0,0,3,1,4])
    print(result)
