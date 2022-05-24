from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 双指针
        MAX_INT = 2**31-1
        left = 0
        res = MAX_INT
        n = len(nums)
        tmp_sum = 0
        for right in range(n):
            tmp_sum += nums[right]
            while tmp_sum >= target:
                res = min(res, right-left+1)
                tmp_sum -= nums[left]
                left += 1
        if res!=MAX_INT:
            return res
        else:
            return 0

if __name__ == '__main__':
    s = Solution()
    # result = s.minSubArrayLen(target=7, nums=[2,3,1,2,4,3])
    result = s.minSubArrayLen(target=4, nums=[1,4,4])
    # result = s.minSubArrayLen(target=11, nums=[1,1,1,1,1,1,1,1])
    print(result)
