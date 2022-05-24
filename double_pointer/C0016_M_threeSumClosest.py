class Solution:
    def threeSumClosest(self, nums, target):
        """
        :param nums:List[int]
        :param target:int
        :return:int
        3 <= nums.length <= 1000
        -1000 <= nums[i] <= 1000
        -104 <= target <= 104
        """
        n = len(nums)
        ans = 0
        minimum = 2**31-1
        nums.sort()
        maxmax = nums[n-1]+nums[n-2]+nums[n-3]
        minmin = nums[0]+nums[1]+nums[2]
        if target > maxmax:
            print("ABOVE")
            return maxmax
        elif target < minmin:
            print("BENEATH")
            return minmin
        else:
            for ii in range(n):
                """下面和之前一样"""
                # 跳过遍历时的全同项目
                if ii > 0 and nums[ii] == nums[ii - 1]:
                    continue
                left = ii + 1
                right = n - 1
                while left < right:
                    if nums[ii] + nums[left] + nums[right] == target:
                        return target
                    elif nums[ii] + nums[left] + nums[right] > target:
                        tmp_minimum = abs(nums[ii] + nums[left] + nums[right] - target)
                        if tmp_minimum < minimum:
                            ans = nums[ii] + nums[left] + nums[right]
                            minimum = tmp_minimum
                        while left < right:
                            right -= 1
                            if nums[right]!=nums[right+1]:
                                break
                    else:
                        tmp_minimum = abs(nums[ii] + nums[left] + nums[right] - target)
                        if tmp_minimum < minimum:
                            ans = nums[ii] + nums[left] + nums[right]
                            minimum = tmp_minimum
                        while left<right:
                            left += 1
                            if nums[left]!=nums[left-1]:
                                break
        return ans



if __name__ == "__main__":
    s = Solution()

    result = s.threeSumClosest([-4, -3, 2, 3, 4, 6, 8], 13)
    print(result)
    result = s.threeSumClosest([0, 0, 0], -7)
    print(result)  # []
