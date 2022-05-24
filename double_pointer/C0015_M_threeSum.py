class Solution:
    def threeSum(self, nums):
        """
        :param nums:List[int]
        :return:List[List[int]]
        """
        n = len(nums)
        if n < 3:
            # 总数小于3直接返回空
            return []
        else:
            ans = []
            nums.sort()
            for ii in range(n):
                if nums[ii] > 0:
                    return ans
                # 跳过遍历时的全同项目
                if ii>0 and nums[ii]==nums[ii-1]:
                    continue
                left = ii+1
                right = n-1
                while left < right:
                    if nums[ii]+nums[left]+nums[right] == 0:
                        ans.append([nums[ii], nums[left], nums[right]])
                        while left < right: # 跳过遍历时的全同项目
                            left += 1
                            if nums[left]!=nums[left-1]:
                                break
                        while left < right: # 跳过遍历时的全同项目
                            right -= 1
                            if nums[right]!=nums[right+1]:
                                break
                    elif nums[ii]+nums[left]+nums[right]>0:
                        right -= 1
                    else:
                        left += 1
            return ans


if __name__ == "__main__":
    s = Solution()
    result = s.threeSum([0, 0])
    # print(result)  # []
    result = s.threeSum([-4, -1, -1, -1, 0, 1, 2])
    print(result)  # [[-1,-1,2],[-1,0,1]]
    result = s.threeSum([-4, -2, -2, -1, -1, 0, 4, 5, 6, 6])
    print(result)  # [[-1,-1,2],[-1,0,1]]
    result = s.threeSum([0,0,0])
    print(result)