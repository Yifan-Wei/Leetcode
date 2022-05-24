from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 单调栈, 求最近的临近升高点
        n = len(temperatures)
        stack = []
        res = [0] * n
        for ii in range(n-1,-1,-1):
            # 只要弄清楚何时弹出栈顶即可:
            # 由于是要求最近的上升点, 先进栈的小于等于的值是可以弹出的, 更大的值不能弹出
            while stack and temperatures[ii] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                res[ii] = stack[-1] - ii
            else:
                res[ii] = 0
            stack.append(ii)
        return res

if __name__ == '__main__':
    s = Solution()
    # result = s.dailyTemperatures([73,74,75,71,69,72,76,73])
    result = s.dailyTemperatures([89,62,70,58,47,47,46,76,100,70])
    print(result)
