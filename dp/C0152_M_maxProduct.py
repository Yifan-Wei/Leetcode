from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp_positive = [0] * n
        dp_negative = [0] * n
        res = nums[0]
        dp_positive[0] = nums[0]
        dp_negative[0] = nums[0]
        for ii in range(1, n):
            dp_positive[ii] = max(dp_positive[ii-1]*nums[ii], dp_negative[ii-1]*nums[ii], nums[ii])
            dp_negative[ii] = min(dp_positive[ii-1]*nums[ii], dp_negative[ii-1]*nums[ii], nums[ii])
            res = max(res, dp_positive[ii])
        # print(dp_positive)
        # print(dp_negative)
        return res


if __name__ == '__main__':
    s = Solution()
    result = s.maxProduct([2,3,-2,4])
    print(result)
