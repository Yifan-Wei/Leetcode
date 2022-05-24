class Solution:
    def case1_removeElement(self, nums: list, val: int) -> int:
        """
        :param nums: List[int]
        :param val:
        :return:
        """
        if not len(nums):
            return 0
        elif len(nums) == 1:
            if nums[0] == val:
                nums = []
                return 0
            else:
                return 1
        else:
            ans = 0
            left = 0
            right = len(nums)-1
            while left < right:
                if nums[right] == val:
                    right -= 1
                    continue
                if nums[left] == val:
                    tmp = nums[left]
                    nums[left]=nums[right]
                    nums[right] = tmp
                    right -= 1
                if left < right:
                    left += 1
            while right >=0:
                if nums[right]==val:
                    right -= 1
                else:
                    break
            nums = nums[:right+1]
            return right+1


    def removeElement(self, nums: list, val: int) -> int:
        if nums is None or len(nums)==0:
            return 0
        jj =0
        for ii in range(len(nums)):
            if nums[ii]!=val:
                nums[jj]=nums[ii]
                jj += 1
        nums = nums[:jj]
        return jj

if __name__ == "__main__":
    s = Solution()
    result = s.removeElement([1, 1], 1)
    print(result)
    result = s.removeElement([4,5],4)
    print(result)
    result = s.removeElement([1,2,3,4,5,6,7], 7)
    print(result)

