class Solution:
    from typing import List
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        O(n) + 常数空间 -> 修改输入列表
        对于一个长度为N的数组, 没有出现的最小正整数只可能在[1, N+1]之间
        将输入列表转换为哈希表
        # 纯算法题, 利用输入结构的更改制作哈希表
        :param nums:
        :return:
        """
        for ii in range(len(nums)):
            if nums[ii]<=0:
                nums[ii] = len(nums)+1
        for ii in range(len(nums)):
            if abs(nums[ii])<=len(nums):
                if nums[abs(nums[ii])-1] >0:
                    nums[abs(nums[ii])-1] = nums[abs(nums[ii])-1] * -1
        for ii in range(len(nums)):
            if nums[ii]>0:
                return ii+1
        return len(nums)+1

if __name__ == "__main__":
    s = Solution()
    res = s.firstMissingPositive([1,1])
    print(res)