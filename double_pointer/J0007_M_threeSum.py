from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        # ----------------------------
        if n<=2: return []
        # ----------------------------
        res = []
        nums.sort()
        for ii in range(n-2):
            # 排序过后, 后面的结果已经顺序, 不用再选了
            if nums[ii] > 0:
                break
            # 跳过重复项目
            if ii > 0 and nums[ii] == nums[ii-1]:
                continue
            left = ii+1
            right = n-1
            # 二分法逼近
            while left<right:
                if nums[ii]+nums[left]+nums[right]==0:
                    res.append([nums[ii],nums[left],nums[right]])
                    # 跳过重复项目
                    while left<right:
                        left+=1
                        if nums[left]!=nums[left-1]:
                            break
                    # 跳过重复项目
                    while left<right:
                        right-=1
                        if nums[right]!=nums[right+1]:
                            break
                elif nums[ii]+nums[left]+nums[right]>0:
                    right -= 1
                else:
                    left += 1
        return res


if __name__ == '__main__':
    s = Solution()
    result = s.threeSum([0, 0])
    # print(result)  # []
    result = s.threeSum([-4, -1, -1, -1, 0, 1, 2])
    # print(result)  # [[-1,-1,2],[-1,0,1]]
    # result = s.threeSum([-4, -2, -2, -1, -1, 0, 4, 5, 6, 6])
    # print(result)  # [[-1,-1,2],[-1,0,1]]
    # result = s.threeSum([0,0,0])
    print(result)