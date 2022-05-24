from typing import List
from S0000_swap import *

class Solution:
    def selectionSort(self, nums):
        # O(N**2) O(1)
        # 交换次数更少: O(N)
        n = len(nums)
        for ii in range(n):
            print(nums)
            minIndex = ii
            for jj in range(ii+1,n):
                # 每一轮选择最小的元素
                if nums[jj] < nums[minIndex]:
                    minIndex = jj
            # 如果这个元素不是ii, 则交换至队列首
            if minIndex!=ii:
                tmp = nums[ii]
                nums[ii] = nums[minIndex]
                nums[minIndex] = tmp

    def biselectionSort(self, nums):
        n = len(nums)
        for ii in range(n):
            print(nums)
            if ii>n-ii:
                break
            minIndex, maxIndex=ii,ii
            for jj in range(ii+1, n-ii):
                if nums[jj]<nums[minIndex]:
                    minIndex = jj
                if nums[jj]>nums[maxIndex]:
                    maxIndex = jj
            if minIndex == maxIndex:
                break
            if minIndex!=ii:
                nums[ii], nums[minIndex] = swap_tmp(nums[ii], nums[minIndex])
            if maxIndex==ii:
                maxIndex = minIndex
            if maxIndex!=ii:
                nums[n-ii-1], nums[maxIndex] = swap_tmp(nums[n-ii-1], nums[maxIndex])


if __name__ == '__main__':
    s = Solution()
    result = s.biselectionSort([8,7,6,5,4,3,2,1])
    print(result)
