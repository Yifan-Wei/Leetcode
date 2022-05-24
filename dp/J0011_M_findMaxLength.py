from typing import List

class Solution:
    # 1 <= nums.length <= 105
    # nums[i]不是0就是1
    def findMaxLength(self, nums: List[int]) -> int:
        # 前缀和+HASH
        n = len(nums)
        max_len = 0
        dp_imp = [0] * (n+1)
        hash_map = {}
        hash_map[0] = 0
        for ii in range(n):
            if nums[ii]:
                dp_imp[ii+1] = dp_imp[ii] + 1
            else:
                dp_imp[ii+1] = dp_imp[ii] - 1
            # 先找-----------------------
            if dp_imp[ii+1] in hash_map.keys():
                first_match = hash_map[dp_imp[ii+1]]
                max_len = max(max_len, ii-first_match+1)
            # 再存-----------------------
            else:
                hash_map[dp_imp[ii+1]] = ii+1
            # for jj in range(0, ii):
            #     if (ii-jj+1) < max_len:
            #         break
            #     print(dp_imp[ii+1], dp_imp[jj], max_len)
            #     if dp_imp[ii + 1] == dp_imp[jj]:
            #         max_len = max(max_len, ii-jj+1)
        # print(dp_imp)
        # print(hash_map)
        return max_len

if __name__ == '__main__':
    s = Solution()
    # result = s.findMaxLength([0, 1, 1])  # ->2
    result = s.findMaxLength([0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1])  # ->4
    print(result)
