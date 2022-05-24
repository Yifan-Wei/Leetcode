class Solution:
    """给你一个长度为 n 的整数数组 nums ，其中 nums 的所有整数都在范围 [1, n] 内,
    且每个整数出现 一次 或 两次 。请你找出所有出现 两次 的整数，并以数组形式返回"""
    from typing import List
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for ii in range(len(nums)):
            each = abs(nums[ii])
            if nums[each-1] > 0:
                nums[each-1] = - nums[each-1]
            else:
                res.append(each)
        return res


if __name__ == '__main__':
    s = Solution()
    result = s.findDuplicates([4,3,2,7,8,2,3,1])
    print(result)
