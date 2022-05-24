class Solution:
    from typing import List
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 5 for _ in range(n+1)]
        # 状态0 未进行过任何交易
        # 状态1 买入过1次股票
        # 状态2 买入并出售过1次股票
        # 状态3 二度买入股票
        # 状态4 二度售出股票
        # 以上状态只能顺序递推, 不能跨越递推
        # print(dp)
        dp[0][0] = 0            # 默认第0天不持有股票
        for ii in range(1, n+1):
            # print(ii)
            if ii == 1:
                dp[ii][0] = dp[ii-1][0]
                dp[ii][1] = dp[ii-1][0] - prices[ii-1]
                dp[ii][2] = dp[ii][0]    # 当天买了又卖
                dp[ii][3] = dp[ii][1]    # 当天买了卖了买了卖
            else:
                # 未交易状态只能处于未交易状态
                dp[ii][0] = dp[ii-1][0]
                # 买入1次状态只能从未交易状态变化
                dp[ii][1] = max(dp[ii-1][1], dp[ii-1][0] - prices[ii-1])
                # 卖出1次状态只能从已经买入1次状态变化
                dp[ii][2] = max(dp[ii-1][2], dp[ii-1][1] + prices[ii-1])
                # 买入第2次状态只能从卖出1次状态变化
                dp[ii][3] = max(dp[ii-1][3], dp[ii-1][2] - prices[ii-1])
                # 卖出第2次状态只能从卖出1次状态变化
                dp[ii][4] = max(dp[ii-1][4], dp[ii-1][3] + prices[ii-1])
        # print(dp)
        return max(dp[n])


if __name__ == '__main__':
    s = Solution()
    result = s.maxProfit([3,3,5,0,0,3,1,4])
    # result = s.maxProfit([7,6,4,3,1])
    print(result)
