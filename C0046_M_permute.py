class Solution:
    from typing import List
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1: return [nums]
        res = []
        path = []
        use_dict = {}
        n = len(nums)
        # 不重复
        for each in nums:
            use_dict[each] = 1

        def dfs(path, res):
            if len(path)==n:
                res.append(path.copy())
                return
            for each in nums:
                if use_dict[each] > 0:
                    path.append(each)
                    use_dict[each] = 0
                    dfs(path, res)
                    path.pop(len(path)-1)
                    use_dict[each] = 1

        dfs(path, res)
        return res

if __name__ == "__main__":
    s = Solution()
    result = s.permute([1,2,3,4])
    print(result)