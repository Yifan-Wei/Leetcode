class Solution:
    from typing import List
    def projectionArea(self, grid: List[List[int]]) -> int:
        """
        n == grid.length == grid[i].length
        1 <= n <= 50
        0 <= grid[i][j] <= 50
        """
        # 放置n*n的立方体
        n = len(grid)
        # 俯视图求解
        area1 = 0
        for ii in range(n):
            for jj in range(n):
                if grid[jj][ii] > 0:
                    area1 += 1
        # 侧视图求解
        area2 = 0
        for ii in range(n):
            max_tmp = 0
            for jj in range(n):
                max_tmp = max(max_tmp, grid[jj][ii])
            area2 += max_tmp
        area3 = 0
        for jj in range(n):
            max_tmp = 0
            for ii in range(n):
                max_tmp = max(max_tmp, grid[jj][ii])
            area3 += max_tmp
        # print(area1, area2, area3)
        return area1+area2+area3

if __name__ == '__main__':
    s = Solution()
    result = s.projectionArea([[2]])
    print(result)
