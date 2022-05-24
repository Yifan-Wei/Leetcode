class Solution:
    from typing import List
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
        求在该柱状图中，能够勾勒出来的矩形的最大面积。
        :param heights:
        1 <= heights.length <=10**5
        0 <= heights[i] <= 10**4
        :return:
        """
        res = 0
        n = len(heights)
        # 每个位置左右比他高的最近的点在哪
        # 正着扫一遍, 获取任意位置左侧的最低高度, 再反过来扫一遍
        n = len(heights)
        left, right = [0] * n, [0] * n
        # 单调栈 复杂度O(N) 用于解决最近的大于/小于它的元素, 存储的是下标
        mono_stack = list()
        # 求取左侧第一个小于该柱子的柱子位置left[i]
        for i in range(n):
            while len(mono_stack)>0:
                if heights[mono_stack[-1]] >= heights[i]:
                    mono_stack.pop()
                else:
                    break
            if len(mono_stack)>0:
                left[i] = mono_stack[-1]
            else:
                left[i] = -1
            mono_stack.append(i)
            # print(left)
            # print("i={0}, heights={1}, stack={2}".format(i, heights[i], mono_stack))
        # 单调栈
        mono_stack = list()
        for i in range(n - 1, -1, -1):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else n
            mono_stack.append(i)

        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans

        """
        # 核心思路是对的，但是时间复杂度太高超时
            while jj < n:
                if heights[jj] < heights[ii]:
                    break
                jj += 1
            while kk >= 0:
                if heights[kk] < heights[ii]:
                    break
                kk -= 1
            list[ii] = jj-kk-1
            res = max(res, list[ii]*heights[ii])
        """




        return res

if __name__ == "__main__":
    s = Solution()
    result = s.largestRectangleArea([2,1,5,6,2,3])
    # result = s.largestRectangleArea([1]*(10**4))
    print(result)