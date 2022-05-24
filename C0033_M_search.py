class Solution:
    def search(self, nums, target):
        """
        :param nums:: List[int]
        :param target:: int
        :return: -> int
        """
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1
        # official
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) >> 1
            print(left, right, mid)
            if nums[mid]>nums[right]:
                # 切入左边上升沿
                if target<=nums[mid] and nums[left]<=target:
                    right = mid
                else:
                    left = mid
            else:
                # 切入右边上升沿
                if target<=nums[right] and nums[mid]<=target:
                    left = mid
                else:
                    right = mid
            if left >= right-1:
                if nums[left]==target:
                    return left
                elif nums[right]==target:
                    return right
                else:
                    return -1

if __name__ == "__main__":
    s = Solution()
    result = s.search([1,3], 1)
    print(result)