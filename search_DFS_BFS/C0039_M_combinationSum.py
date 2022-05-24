class Solution:
    def case_combinationSum(self, candidates, target):
        """
        :param candidates:: List[int]
        :param target:: int
        :return:-> List[List[int]]
        """
        dp=[[]]
        for ii in range(1, target+1):
            dp.append([])
            for each in candidates:
                if ii-each == 0:
                    dp[ii].append([each])
                elif ii-each > 0:
                    if dp[ii-each] != []:
                        for each_one in dp[ii-each]:
                            tmp = each_one.copy()
                            if each>=tmp[len(tmp)-1]:
                                tmp.append(each)
                                dp[ii].append(tmp)
        return dp[target]

    from typing import List
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, begin, size, path, res, target):
            print(begin, size, path, res, target)
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return

            for index in range(begin, size):
                dfs(candidates, index, size, path + [candidates[index]], res, target - candidates[index])

        size = len(candidates)
        if size == 0:
            return []
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.case_combinationSum([2,3,5], 8))
