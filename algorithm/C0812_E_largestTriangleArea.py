from typing import List


class Solution:
    # 3 <= points.length <= 50
    # -50 <= points[i][j] <= 50.
    # 结果误差值在 10^-6 以内都认为是正确答案。
    def largestTriangleArea(self, points: List[List[int]]) -> float:

        def area_triangle(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            return abs((1/2)*(x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2))
        max_area = 0
        n = len(points)
        for ii in range(n):
            for jj in range(ii+1,n):
                for kk in range(jj+1,n):
                    # print(ii,jj,kk)
                    max_area = max(max_area, area_triangle(points[ii], points[jj], points[kk]))
        return max_area

if __name__ == '__main__':
    s = Solution()
    result = s.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]])
    print(result)
