class Solution:
    def searchInsert(self, nums, target) -> int:
        if target<nums[0]: return 0
        if target>nums[len(nums)-1]: return len(nums)
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)>>1
            if nums[mid]>=target:
                right = mid - 1
                ans = mid
            else:
                left = mid + 1

        return ans
if __name__ == "__main__":
    s = Solution()
    """
    result = s.searchInsert([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
    print(result)
    result = s.searchInsert([1], 2)
    print(result)
    result = s.searchInsert([1], 0)
    print(result)
    """
    result = s.searchInsert([0, 1, 2, 3, 5, 6, 7, 9], 8)
    print(result)
    result = s.searchInsert([1, 3, 5, 6], 5)
    print(result)
    result = s.searchInsert([1, 3, 5, 6], 2)
    print(result)
    result = s.searchInsert([1, 3, 5, 6], 7)
    print(result)