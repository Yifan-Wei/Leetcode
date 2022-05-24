"""
给定一个长度为 n 的整数数组height。有n条垂线，第 i 条线的两个端点是(i, 0)和(i, height[i])。
找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。
说明：你不能倾斜容器。
"""


class Solution:
    def maxArea(self, height):
        area = 0
        ii = 0
        jj = len(height)-1
        while ii < jj:
            area = max(area, (jj-ii)*min(height[ii], height[jj]))
            if height[ii] > height[jj]:
                jj -= 1
            else:
                ii += 1
        return area

if __name__ == "__main__":
    s = Solution()
    result = s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(result)
    result = s.maxArea([1, 1])
    print(result)