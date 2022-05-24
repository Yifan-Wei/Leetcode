from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        min_left, min_right, max_left, max_right = [-1] * n, [n] * n, [-1] * n, [n] * n
        # -------------------------------------------------------------------------------
        stack = []
        for ii in range(n):
            while stack and nums[ii]<=nums[stack[-1]]:
                min_right[stack.pop()] = ii
            if stack:
                min_left[ii] = stack[-1]
            stack.append(ii)
        stack = []
        for ii in range(n):
            while stack and nums[ii]>=nums[stack[-1]]:
                max_right[stack.pop()] = ii
            if stack:
                max_left[ii] = stack[-1]
            stack.append(ii)
        # ------------------------------------------------------------------------------
        for ii in range(n):
            print(nums[ii], ":", max_left[ii]+1, max_right[ii]-1)

        res = 0
        # Sigma x:(l->ii) * Sigma y:(ii->r)  max[]-min[]
        for ii in range(n):
            res += ((ii-max_left[ii]) * (max_right[ii]-ii) * nums[ii] - (ii-min_left[ii]) * (min_right[ii]-ii) * nums[ii])

        return res


if __name__ == '__main__':
    s = Solution()
    result = s.subArrayRanges([4,-2,-3,4,1])
    print(result)
