class Solution:
    from typing import List
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        1 <= nums.length <= 3 * 10**4
        -10**4 <= nums[i] <= 10**4
        nums 已按升序排列
        :param nums:
        :return:
        """
        n = len(nums)
        if n<=2:
            return n
        slow = 2
        fast = 2
        while fast < len(nums):
            if nums[slow-2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        # print(nums[:slow])
        return slow

if __name__ == "__main__":
    s = Solution()
    result = s.removeDuplicates([0,0,1,1,1,1,2,3,3])
    # result = s.removeDuplicates([1,1,1,2,2,3])
    print(result)
