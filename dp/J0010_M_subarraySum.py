from typing import List
from collections import defaultdict

class Solution:
    # 1 <= nums.length <= 2 * 10**4
    # -1000 <= nums[i] <= 1000
    # -10**7 <= k <= 10**7
    def self_subarraySum(self, nums: List[int], k: int) -> int:
        # 朴素的前缀和方法会超时
        # print(nums)
        res = 0
        n = len(nums)
        dp_sum = [0] * (n+1)
        hash_map = defaultdict()
        hash_map[0] = 1
        # ii = right
        for ii in range(1, n+1):
            index_right = ii-1
            # 计算加和 ------------------------------
            dp_sum[ii] = dp_sum[ii-1] + nums[index_right]
            # 先搜索目标和---------------------------------
            target_dp_sum = dp_sum[ii] - k
            if (target_dp_sum) in hash_map.keys():
                res += hash_map[target_dp_sum]
            # 再计算加和-----------------------------------
            if dp_sum[ii] in hash_map.keys():
                hash_map[dp_sum[ii]] += 1
            else:
                hash_map[dp_sum[ii]] = 1
            # --------------------------------------------
            # print("DEAL WITH {0}th Num: {1}, Now Sum to {2}, Need Sum {3}".format(index_right, nums[index_right],dp_sum[ii],target_dp_sum))
            # print(hash_map)
        return res

    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        hash_map = {}
        hash_map[0] = 1
        # ii = right
        for ii in range(n):
            index_right = ii-1
            # 计算加和 ------------------------------
            if ii:
                nums[ii] += nums[ii-1]
            # 先搜索目标和---------------------------------
            target_dp_sum = nums[ii] - k
            if (target_dp_sum) in hash_map.keys():
                res += hash_map[target_dp_sum]
            # 再计算加和-----------------------------------
            if nums[ii] in hash_map.keys():
                hash_map[nums[ii]] += 1
            else:
                hash_map[nums[ii]] = 1
        # print(nums)
        return res

if __name__ == '__main__':
    s = Solution()
    result = s.subarraySum(nums = [1,2,-1,-2,0,3,-3] , k = 0) # =7
    print(result)
