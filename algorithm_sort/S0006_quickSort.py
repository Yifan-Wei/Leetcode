from typing import List
from S0000_swap import *

class Solution:
    # 3数取中快排
    def quickSortMedian3(self, nums):
        if len(nums)<2: return nums

        def median3(arr, left, right):
            mid = left + (right-left)//2
            # 左中元素大者居中
            if arr[left] > arr[mid]:
                arr[left], arr[mid] = swap(arr[left], arr[mid])
            # 中右元素大者居右
            if arr[mid] > arr[right]:
                arr[mid], arr[right] = swap(arr[mid], arr[right])
            # 前两个操作完成后, 最大在最右
            # 第三个if保证大者在左(即中者在左了)
            if arr[left] < arr[mid]:
                arr[left], arr[mid] = swap(arr[left], arr[mid])

        def iterQuickSortMedian3(arr, left, right):
            if left<right:
                median3(arr, left, right)
                pivot = self.partition(arr, left, right)
                iterQuickSortMedian3(arr, left, pivot-1)
                iterQuickSortMedian3(arr, pivot+1, right)

        iterQuickSortMedian3(nums, 0, len(nums)-1)
        print(nums)

    # 核心方法 partition (要求完成主轴准备, 主轴必须在最左边)
    def partition(self, arr, left, right):
        pivot = left            # 选定一个数作为主轴后, 将主轴置为起始位置
        index = pivot + 1       # 设置index = pivot + 1动态更新最终的主轴下标
        # 下面的过程有点类似选择排序, 但是是选到中间的位置而不是两边
        for ii in range(index, right+1):    # 从左到右将主轴后的所有元素与主轴比较, 小于则交换并后移index
            # print(arr, ii, index)
            if arr[ii] < arr[pivot]:
                arr[index], arr[ii] = swap(arr[index], arr[ii])
                index += 1
        arr[pivot], arr[index-1] = swap(arr[pivot], arr[index-1])
        return index-1

if __name__ == '__main__':
    s = Solution()
    result = s.quickSortMedian3([6,1,3,5,7,9,7,5,3,1])
    print(result)
