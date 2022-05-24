class Solution:
    def removeDuplicates(self, nums: list):
        """
        :param nums: List[int]
        :return:-> int
        """
        if len(nums):
            ans = 0
            ii = 1
            while ii < len(nums):
                if nums[ii]==nums[ii-1]:
                    nums.pop(ii)
                else:
                    ii += 1
            return ii
        else:
            return 0

if __name__ == "__main__":
    # RUN
    s = Solution()
    result = s.removeDuplicates([])
    print(result)

