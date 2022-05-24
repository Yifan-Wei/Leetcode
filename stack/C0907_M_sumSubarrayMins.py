from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [-1] * n
        right = [n] * n
        stack = []
        INF = 10**9 + 7
        for ii in range(n):
            while stack and arr[ii]<=arr[stack[-1]]:
                right[stack.pop()] = ii
            if stack: left[ii] = stack[-1]
            stack.append(ii)
        res = 0
        for ii in range(n):
            # 枚举每个最小值的覆盖范围: 覆盖范围为l-r
            # 但子区间需要满足[x:y+1]中l<=x<=ii, ii<=y<=r
            l, r = left[ii] + 1, right[ii]-1
            # Sigma(x:l->ii)Sigma(y:ii->r) min(arr[x->y])
            # = Sigma(x:l->ii)Sigma(y:ii->r) arr[ii]
            # = (ii-l+1)*(r-ii+1)*arr[ii]
            res += (ii-l+1)*(r-ii+1)*arr[ii]
            res %= INF
        return res


if __name__ == '__main__':
    s = Solution()
    result = s.sumSubarrayMins()
    print(result)
