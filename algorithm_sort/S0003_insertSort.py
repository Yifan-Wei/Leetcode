from typing import List
from S0000_swap import *

class Solution:
    def insertSort(self, nums):
        # 时间O(N**2) 空间O(1)
        # 交换次数O(N)
        n = len(nums)
        for ii in range(1, n):
            target = nums[ii]
            jj = ii-1
            print(nums, target)
            while jj>-1:
                if target < nums[jj]:
                    nums[jj+1] = nums[jj]
                    jj -= 1
                else:
                    break
            if jj != ii-1:
                nums[jj+1] = target
        print(nums)

if __name__ == '__main__':
    s = Solution()
    result = s.insertSort([9,8,7,6,5,4,3,2,1])
    result = s.insertSort([1,7,4,2,6,3,5,8,9])
    print(result)
