from typing import List


class Solution:
    """
    给你一个整数数组nums ，请计算数组的 中心下标 。
    数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。
    如果中心下标位于数组最左端，那么左侧数之和视为 0 ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。
    如果数组有多个中心下标，应该返回 最靠近左边 的那一个。如果数组不存在中心下标，返回 -1
    """
    def pivotIndex(self, nums: List[int]) -> int:
        # 1 <= nums.length <= 10**4
        # -1000 <= nums[i] <= 1000
        n = len(nums)
        for ii in range(n):
            if ii>0:
                nums[ii] += nums[ii-1]
        for ii in range(n):
            if ii > 0:
                if nums[ii-1]==nums[n-1]-nums[ii]:
                    return ii
            else:
                if nums[n-1]-nums[ii] == 0:
                    return ii
        return -1

if __name__ == '__main__':
    s = Solution()
    result = s.pivotIndex([4,3,2,1,-10,0])
    print(result)
