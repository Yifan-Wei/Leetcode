from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # n == nums.length
        # 1 <= nums.length <= 10**5
        # -10**9 <= nums[i] <= 10**9
        left = min(nums)
        right = max(nums)
        def abs_sum(arr, target):
            tmp = 0
            for ii in range(len(arr)):
                tmp += abs(arr[ii]-target)
            return tmp

        def get_mid(left, right):
            return left + ((right - left) >> 1)

        mid = get_mid(left, right)
        mid_abs_sum = abs_sum(nums, mid)
        while True:
            left_mid = get_mid(left, mid)
            right_mid = get_mid(mid, right)
            leftmid_abs_sum = abs_sum(nums, left_mid)
            rightmid_abs_sum = abs_sum(nums, right_mid)
            if left_mid == right_mid:
                break
            # print(leftmid_abs_sum, mid_abs_sum, rightmid_abs_sum)
            if leftmid_abs_sum <= mid_abs_sum:
                right = mid
                mid = left_mid
                mid_abs_sum = leftmid_abs_sum
            elif rightmid_abs_sum <= mid_abs_sum:
                left = mid
                mid = right_mid
                mid_abs_sum = rightmid_abs_sum
            else:
                left = left_mid
                right = right_mid
        return min(min(mid_abs_sum, leftmid_abs_sum), rightmid_abs_sum)


if __name__ == '__main__':
    s = Solution()
    result = s.minMoves2([2])
    print(result)
