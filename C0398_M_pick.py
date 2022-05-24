class Solution:
    from typing import List

    def __init__(self, nums: List[int]):
        """
         1<nums.length<=2*10**4, -2**31<=nums[i]<=2**31-1
        :param nums:
        """
        self.pick_dict = {}
        for ii in range(len(nums)):
            if nums[ii] in self.pick_dict.keys():
                self.pick_dict[nums[ii]].append(ii)
            else:
                self.pick_dict[nums[ii]] = [ii]
        return

    def pick(self, target: int) -> int:
        """
        最多调用10**4次
        :param target:
        :return:
        """
        from random import randint
        n = len(self.pick_dict[target])
        res = self.pick_dict[target][randint(0,n-1)]
        return res

class Solution2:
    from typing import List
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        # 蓄水池抽样/水塘抽样
        from random import randrange
        ans = cnt = 0
        for i, num in enumerate(self.nums):
            if num == target:
                cnt += 1  # 第 cnt 次遇到 target
                if randrange(cnt) == 0:
                    ans = i
        # print(ans)
        return ans


# Your Solution object will be instantiated and called as such:
obj = Solution2([1, 2, 3, 3, 3])
param_1 = obj.pick(1)
# param_1 = obj.pick(3)
# param_1 = obj.pick(3)