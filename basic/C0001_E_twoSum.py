class Solution:
    def twoSum(self, nums, target):
        result = []
        for ii in range(len(nums)):
            for jj in range(ii+1, len(nums)):
                if nums[ii]+nums[jj]==target:
                    result.append(ii)
                    result.append(jj)
                    break
        return result

if __name__ == "__main__":
    s = Solution()
    result = s.twoSum([3, 2, 4], 13)
    print(result)