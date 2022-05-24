class Solution:
    def combinationSum2(self, candidates, target):
        """
        给定一个候选人编号集合candidates, 和一个目标数target, 要求找出candidate中所有数字和为target的组合
        candidate中所有数字都只能使用1次
        :param candidates:
        :param target:
        :return:
        """
        def dfs(candidates, begin, path, res, target):
            print(begin,path,res,target)
            if target<0:
                return
            if target==0:
                if not (path in res):
                    res.append(path)
                return
            print(candidates[begin:len(candidates)])
            """
            下方代码有两个关键:
            1. ii>begin and candidates[ii]==candidates[ii-1] 剪枝是为了避免解集中重复元素
            已排序的形如:[1,1,1,4] target=6中, 先选择[0]1, 之后再选择[1]1, 和选择[2]1是全同的, 由于每个元素都可以使用
            并不禁止使用当前的值(begin), 但如果不使用当前值, 使用之后的值与当前相同是无意义的
            在连续使用的过程中, 可以顺序使用[0]1 [1]1 [2]1, 并不排斥这种情况
            2. dfs(ii+1), 是因为题设中同一元素不能重复选取
            """
            for ii in range(begin, len(candidates)):
                if ii > begin and candidates[ii] == candidates[ii-1]:
                    continue
                dfs(candidates, ii+1, path+[candidates[ii]], res, target-candidates[ii])

        candidates.sort()
        res = []
        path = []
        dfs(candidates, 0, path, res, target)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 27))
    # print(s.combinationSum2([10,1,2,7,6,1,5,1], 8))