class Solution:
    from typing import List
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 连续输出, 一眼滑动窗口
        res = 0
        n = len(nums)
        ii = 0
        total = 1
        for jj in range(n):
            # 加入新值
            total *= nums[jj]
            # print(ii,jj)
            while total >= k and ii<=jj:
                total /= nums[ii]
                ii += 1
            res += (jj+1-ii)
        return res

if __name__ == '__main__':
    s = Solution()
    result = s.numSubarrayProductLessThanK([1,2,3], 3)
    print(result)
