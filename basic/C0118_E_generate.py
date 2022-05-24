class Solution:
    from typing import List
    def generate(self, numRows: int) -> List[List[int]]:
        # 杨辉三角初始化
        # -------------------------------------
        res = []
        for ii in range(numRows):
            if not ii:
                res.append([1])
            else:
                res.append([1]+[0]*(ii-1)+[1])
        # --------------------------------------
        # 仅2行时特殊处理
        if numRows<=2: return res
        # --------------------------------------
        for ii in range(2,numRows):
            for jj in range(1,ii):
                res[ii][jj] = res[ii-1][jj-1]+res[ii-1][jj]
        return res

if __name__ == '__main__':
    s = Solution()
    result = s.generate(3)
    print(result)
