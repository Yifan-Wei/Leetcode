class Solution:
    def searchRange(self, nums, target):
        """
        :param nums: List[int]
        :param target:  int
        :return:  List[int]
        """
        length = len(nums)
        # 特殊处理
        if length == 0: return [-1, -1]
        if length == 1:
            if nums[0] != target:
                return [-1, -1]
            else:
                return [0, 0]

        #
        def binary_search(target, lower):
            # lower是为了方便代码复用
            left = 0
            right = length-1
            ans = length
            while left<=right:
                mid = (left+right)>>1
                if nums[mid]>target or (lower and nums[mid]>=target):
                    right = mid - 1
                    ans = mid
                else:
                    left = mid + 1
            return ans

        left_index = binary_search(target, True)
        right_index = binary_search(target, False) - 1
        if left_index<=right_index and right_index<length and nums[left_index]==target and nums[right_index]==target:
            return [left_index, right_index]
        else:
            return [-1, -1]


if __name__ == "__main__":
    s = Solution()
    result = s.searchRange([0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 10, 10, 10, 10], 10)
    print(result)
    result = s.searchRange([], 1)
    print(result)
    result = s.searchRange([1], 1)
    print(result)
    result = s.searchRange([1], -1)
    print(result)
    result = s.searchRange([1, 1, 1], 1)
    print(result)
    result = s.searchRange([1, 1, 1, 1, 1, 1, 1, 1, 1], 1)
    print(result)
    result = s.searchRange([5, 5, 5, 5, 5, 7, 7, 8, 8, 10, 10, 10, 10, 10], 5)
    print(result)
    result = s.searchRange([5, 5, 5, 5, 5, 7, 7, 8, 8, 10, 10, 10, 10, 10], 6)
    print(result)
    result = s.searchRange([5, 5, 5, 5, 5, 7, 7, 8, 8, 10, 10, 10, 10, 10], 7)
    print(result)