class Solution:
    from typing import List
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 动态规划
        res = []
        h = len(heights)
        w = len(heights[0])
        # pacific = 1
        # atlantci = 2
        dp = [[0] * w for _ in range(h)]
        for ii in range(w):
            dp[0][ii] = 1
            dp[h-1][ii] = 2
        for jj in range(h):
            dp[jj][0] = 1
            dp[jj][w-1] = 2
        dp[h-1][0] = 3
        dp[0][w-1] = 3

        def stream_discuss(dut, cmp):
            # print(dut, cmp)
            if dut == 3 or cmp ==3:
                return 3
            if dut == 0:
                return cmp
            if cmp == 0:
                return dut
            if dut+cmp == 3:
                return 3
            if dut == cmp:
                return dut

        for jj in range(w):
            for ii in range(h):
                # print(ii, jj, dp[ii-1][jj], dp[ii][jj-1])
                if ii-1>=0 and heights[ii][jj] >= heights[ii-1][jj]:
                   dp[ii][jj] = stream_discuss(dp[ii][jj],dp[ii-1][jj])
                if jj-1>=0 and heights[ii][jj] >= heights[ii][jj-1]:
                   dp[ii][jj] = stream_discuss(dp[ii][jj],dp[ii][jj-1])
        # for each in dp:
            # print(each)
        # print("-------------------------")
        for jj in range(w-1,-1,-1):
            for ii in range(h-1,-1,-1):
                # print(ii+1, h-1, jj+1, w-1)
                if ii<h-1 and heights[ii][jj] >= heights[ii+1][jj]:
                   dp[ii][jj] = stream_discuss(dp[ii][jj],dp[ii+1][jj])
                if jj<w-1 and heights[ii][jj] >= heights[ii][jj+1]:
                   dp[ii][jj] = stream_discuss(dp[ii][jj],dp[ii][jj+1])
        # for each in dp:
            # print(each)
        # --------------------------------------------------------------
        for jj in range(w):
            for ii in range(h):
                # print(ii, jj, dp[ii-1][jj], dp[ii][jj-1])
                if ii-1>=0 and heights[ii][jj] >= heights[ii-1][jj]:
                   dp[ii][jj] = stream_discuss(dp[ii][jj],dp[ii-1][jj])
                if jj-1>=0 and heights[ii][jj] >= heights[ii][jj-1]:
                   dp[ii][jj] = stream_discuss(dp[ii][jj],dp[ii][jj-1])
        # print("-------------------------")
        # for each in dp:
            # print(each)
        # --------------------------------------------------------------
        for ii in range(h):
            for jj in range(w):
                if dp[ii][jj]==3:
                    res.append([ii,jj])
        return res

    from typing import List
    def pacificAtlantic2(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def search(starts):
            visited = set()

            def dfs(x: int, y: int):
                if (x, y) in visited:
                    return
                visited.add((x, y))
                for nx, ny in ((x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)):
                    if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y]:
                        dfs(nx, ny)

            for x, y in starts:
                dfs(x, y)
            return visited

        pacific = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m - 1, i) for i in range(n)] + [(i, n - 1) for i in range(m - 1)]
        print(pacific)
        return list(map(list, search(pacific) & search(atlantic)))

if __name__ == '__main__':
    s = Solution()
    result = s.pacificAtlantic2([[[8,13,11,18,14,16,16,4,4,8,10,11,1,19,7],[2,9,15,16,14,5,8,15,9,5,14,6,10,15,5],[15,16,17,10,3,6,3,4,2,17,0,12,4,1,3],[13,6,13,15,15,16,4,10,7,4,19,19,4,9,13],[7,1,9,14,9,11,5,4,15,19,6,0,0,13,5],[9,9,15,12,15,5,1,1,18,1,2,16,15,18,9],[13,0,4,18,12,0,11,0,1,15,1,15,4,2,0],[11,13,12,16,9,18,6,8,18,1,5,12,17,13,5],[7,17,2,5,0,17,9,18,4,13,6,13,7,2,1],[2,3,9,0,19,6,6,15,14,4,8,1,19,5,9],[3,10,5,11,7,14,1,5,3,19,12,5,2,13,16],[0,8,10,18,17,5,5,8,2,11,5,16,4,9,14],[15,9,16,18,9,5,2,5,13,3,10,19,9,14,3],[12,11,16,1,10,12,6,18,6,6,18,10,9,5,2],[17,9,6,6,14,9,2,2,13,13,15,17,15,3,14],[18,14,12,6,18,16,4,10,19,5,6,8,9,1,6]]])
    # result = s.pacificAtlantic([[10,10,10],[10,1,10],[10,10,10]])
    # result = s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
    print(result)
