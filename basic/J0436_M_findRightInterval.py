from typing import List
from functools import cmp_to_key

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # 1 <=intervals.length <= 2 * 10**4
        # intervals[i].length == 2
        # -10**6 <= starti <= endi <= 10**6
        # 每个间隔的起点都不相同
        index_dict = {}
        n = len(intervals)
        res = [-1] * n
        for ii, each in enumerate(intervals):
            index_dict[each[0]] = ii

        def cmp(indice1, indice2):
            if indice1[0]<indice2[0]:
                return -1
            else:
                return 1
        intervals.sort(key=cmp_to_key(cmp))
        print(intervals)
        for ii, each in enumerate(intervals):
            starti = each[0]
            endi = each[1]
            index = index_dict[starti]
            if ii==n-1:
                res[index]=-1
                continue
            print(each)
            left = ii
            right = n-1
            left_start = intervals[left][0]
            right_start = intervals[right][0]
            # 排序后的最大左边界小于你的右边界, 则不可能有结果
            if right_start < endi:
                print("IMPOSSIBLE")
                res[index] = -1
                continue
            # 排序后的左边界就符合你的右边界要求, 则不可能有比排序最近的更小的, 直接返回
            if left_start >= endi:
                print("INSTANT FIND")
                res[index] = index_dict[left_start]
                continue
            while left<right:
                mid = left + ((right-left)>>1)
                print(left, mid, right)
                mid_start = intervals[mid][0]
                if mid_start >= endi:
                    right = mid
                elif mid_start < endi:
                    left = mid+1
            res[index] = index_dict[intervals[right][0]]
        return res

    def biselect(self, nums, target):
        left = 0
        right = len(nums)-1
        while left < right:
            mid = left + ((right - left) >> 1)
            print(nums[left],nums[mid],nums[right])
            mid_start = nums[mid]
            if mid_start >= target:
                right = mid
            elif mid_start < target:
                left = mid + 1
        return nums[right]


if __name__ == '__main__':
    s = Solution()
    result = s.findRightInterval([[3, 4], [2, 3], [1, 2]])
    # result = s.findRightInterval([[1,1],[3,4]])
    # result = s.biselect([1,4,5,7,8,9],7)
    print(result)
