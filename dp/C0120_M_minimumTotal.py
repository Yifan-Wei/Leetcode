class Solution:
    """
    给定一个三角形 triangle ，找出自顶向下的最小路径和。
    每一步只能移动到下一行中相邻的结点上。
    相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
    也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
    """
    from typing import List
    # 搜索会超时
    def backtrace_minimumTotal(self, triangle: List[List[int]]) -> int:
        # 超时
        height = len(triangle)-1
        # print(height)
        def dfs(h, x, now_sum):
            # 搜索到该节点, 加入该节点数值
            now_sum += triangle[h][x]
            # print(h, x, now_sum)
            # 如果抵达最深, 返回当前路径和
            if h == height:
                return now_sum
            # 否则返回下一层可搜索节点最小路径和
            else:
                return min(dfs(h+1, x, now_sum), dfs(h+1, x+1, now_sum))
        return dfs(0, 0, 0)
    # 自底端向上的动态规划
    def dp_minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * (ii+1) for ii in range(n)]
        # print(dp)
        for ii in range(n-2, -1, -1):
            for jj in range(ii+1):
                dp[ii][jj] = min(dp[ii+1][jj] + triangle[ii+1][jj], dp[ii+1][jj+1] + triangle[ii+1][jj+1])
                # print(ii, jj, dp[ii][jj])
        return dp[0][0]+triangle[0][0]
    # 在原始结构上进行动态规划
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for ii in range(len(triangle)-2, -1, -1):
            for jj in range(ii+1):
                triangle[ii][jj] += min(triangle[ii+1][jj], triangle[ii+1][jj+1])
        return triangle[0][0]

if __name__ == '__main__':
    s = Solution()
    result = s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
    # result = s.minimumTotal([[-10]])
    print(result)
