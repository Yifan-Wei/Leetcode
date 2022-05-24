from typing import List

class Solution:
    def bubbleSort(self, nums):
        # 稳定性
        # O(N**2) + O(1)
        # 交换次数O(N**2)
        # 将最大/最小的数字像泡泡一样浮到队列的头/尾
        if (not nums) or (len(nums)<2):
            return nums
        # ---------------------------------------------------------
        for ii in range(len(nums)):
            print(nums)
            flag_swapped = False
            for jj in range(len(nums)-ii-1):
                if nums[jj] > nums[jj+1]:
                    nums[jj], nums[jj+1] = swap_tmp(nums[jj], nums[jj+1])
                    flag_swapped = True
            if not flag_swapped:
                break

if __name__ == '__main__':
    s = Solution()
    result = s.bubbleSort([9,1,2,3,4,5,6,7])
    print(result)
