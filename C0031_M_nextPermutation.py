class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        if len(nums) == 2:
            tmp = nums[0]
            nums[0] = nums[1]
            nums[1] = tmp
            return
        right = len(nums)-1
        left = right - 1
        # 最简单的情形, 最后两位可以反过来
        if nums[left] < nums[right]:
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp
            # print(nums)
            return
        else:
            mid = left
            left = mid - 1
            while left >= 0:
                if nums[left] >= nums[mid]:
                    mid = left
                    left = mid - 1
                    if left < 0:            # 没找到mid
                        for ii in range(0, len(nums) - 1):
                            for jj in range(ii + 1, len(nums)):
                                if nums[ii] > nums[jj]:
                                    tmp = nums[ii]
                                    nums[ii] = nums[jj]
                                    nums[jj] = tmp
                        return
                else:
                    while left < right:
                        if nums[left] < nums[right]:
                            print(nums[left], nums[mid], nums[right])
                            tmp = nums[left]
                            nums[left] = nums[right]
                            nums[right] = tmp
                            for ii in range(mid, len(nums)-1):
                                for jj in range(ii+1, len(nums)):
                                    if nums[ii] > nums[jj]:
                                        tmp = nums[ii]
                                        nums[ii] = nums[jj]
                                        nums[jj] = tmp
                            # print(nums)
                            return
                        else:
                            right -= 1
        # print(nums)


if __name__ == "__main__":
    a = Solution()
    ask = [3,2,1]
    # a.nextPermutation([1, 5, 6, 4, 3, 2])
    a.nextPermutation(ask)
    print(ask)
    # a.nextPermutation([6, 5, 4, 3, 2, 1])
    # a.nextPermutation([1, 4, 4, 6, 3, 1])
    # 1, 3, 3 -> 3, 1, 3 -> 3, 3, 1
    # 1, 2, 3 -> 1, 3, 2 -> 2, 1, 3
    # 1, 2, 3, 4 -> 1, 2, 4, 3 -> 1, 3, 2, 4 -> 1, 3, 4, 2 -> 1, 4, 2, 3
    # 1, 5, 2, 4, 3 -> 1, 5, 3, 2, 4