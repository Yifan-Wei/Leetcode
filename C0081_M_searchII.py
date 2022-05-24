class Solution:
    from typing import List
    def search(self, nums: List[int], target: int) -> bool:
        """
        :param nums:: List[int]
        :param target:: int
        :return: -> int
        """
        if len(nums)==1:
            if nums[0]==target:
                return True
            else:
                return False
        # official
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) >> 1
            # print(left, right, mid)
            if nums[mid]==nums[left] and nums[mid]==nums[right]:
                # 无法判断的情形, 两边缩进
                left += 1
                right -= 1
            elif nums[mid]>nums[right]:
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
                    return True
                elif nums[right]==target:
                    return True
                else:
                    return False

if __name__ == "__main__":
    s = Solution()
    result = s.search([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], 2)
    print(result)