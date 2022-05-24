from typing import List


class Solution:
    # 自顶向下非原地
    def mergeSort(self,nums):
        # 时间 O(NlogN), 空间O(N)
        if len(nums)<2:
            return nums
        tmp_nums = [0] * len(nums)
        self.iterMergeSort(nums, tmp_nums,0, len(nums)-1)

    # 自底向上非原地
    def mergeSortBU(self, nums):
        if len(nums)<2:
            return nums
        tmp_nums = [0] * len(nums)
        gap = 1
        while gap<len(nums):
            left = 0
            while left<len(nums)-gap:
                self.merge(nums, tmp_nums, left, left+gap-1, min(left+2*gap-1, len(nums)-1))
                left += 2 * gap
            gap *= 2

    def iterMergeSort(self, nums, tmp_nums, left, right):
        if left < right:
            mid = left + (right-left)//2
            self.iterMergeSort(nums, tmp_nums, left, mid)
            self.iterMergeSort(nums, tmp_nums, mid+1, right)
            self.merge(nums, tmp_nums, left, mid, right)

    # 非原地核心函数
    def merge(self, nums, tmp_nums, leftPos, leftEnd, rightEnd):
        rightPos = leftEnd + 1
        startIdx = leftPos
        tmpPos = leftPos
        print("merge", leftPos, rightPos)
        print(nums[leftPos:rightPos], nums[rightPos:rightEnd+1])
        while leftPos <= leftEnd and rightPos <= rightEnd:
            if nums[leftPos] <= nums[rightPos]:
                tmp_nums[tmpPos] = nums[leftPos]
                tmpPos += 1
                leftPos += 1
            else:
                tmp_nums[tmpPos] = nums[rightPos]
                tmpPos += 1
                rightPos += 1
        # 比较完成后若左数组还有剩余，则将其添加到tmp_nums剩余空间
        while leftPos<=leftEnd:
            tmp_nums[tmpPos] = nums[leftPos]
            tmpPos += 1
            leftPos += 1
        # 比较完成后若右数组还有剩余，则将其添加到tmpArr剩余空间
        while rightPos<=rightEnd:
            tmp_nums[tmpPos] = nums[rightPos]
            tmpPos += 1
            rightPos += 1
        # 将临时空间拷贝回去
        for ii in range(startIdx, rightEnd+1):
            nums[ii] = tmp_nums[ii]


if __name__ == '__main__':
    s = Solution()
    result = s.mergeSortBU([9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9])
    print(result)
