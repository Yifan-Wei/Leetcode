class Solution:
    from typing import List
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1: return [nums]
        nums.sort()
        res = []
        path = []
        use_dict = {}
        n = len(nums)
        # 不重复
        for each in nums:
            if each in use_dict.keys():
                use_dict[each] = use_dict[each] + 1
            else:
                use_dict[each] = 1

        def dfs(path, res):
            if len(path)==n:
                res.append(path.copy())
                return
            for ii in range(n):
                each = nums[ii]
                if ii>0 and nums[ii]==nums[ii-1]:
                    continue
                if use_dict[each] > 0:
                    path.append(each)
                    use_dict[each] = use_dict[each]-1
                    dfs(path, res)
                    path.pop(len(path)-1)
                    use_dict[each] = use_dict[each]+1
        dfs(path, res)
        return res

if __name__ == "__main__":
    s = Solution()
    result = s.permuteUnique([1,1,2])
    print(result)