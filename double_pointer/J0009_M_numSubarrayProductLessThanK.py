from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 双指针
        left = 0
        res = 0
        n = len(nums)
        tmp = 1
        for right in range(n):
            tmp *= nums[right]
            # print(left, right)
            while tmp >= k and left<=right:
                tmp /= nums[left]
                left += 1
                if left == right:
                    break
            if tmp < k:
                # for ii in range(left, right+1):
                #     res.append(nums[ii:right+1])
                res += (right-left+1)
        return res

if __name__ == '__main__':
    s = Solution()
    result = s.numSubarrayProductLessThanK(nums=[10,100,5,2,6,10], k=100)
    # result = s.numSubarrayProductLessThanK([1,2,3,0,1,2,3], 3)
    # result = s.minSubArrayLen(target=11, nums=[1,1,1,1,1,1,1,1])
    print(result)
