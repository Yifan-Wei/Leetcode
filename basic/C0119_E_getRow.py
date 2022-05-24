class Solution:
    from typing import List
    def getRow(self, rowIndex: int) -> List[int]:
        # 杨辉三角初始化
        rowIndex += 1
        # -------------------------------------
        res = []
        for ii in range(rowIndex):
            if not ii:
                res.append([1])
            else:
                res.append([1]+[0]*(ii-1)+[1])
        # --------------------------------------
        # 仅2行时特殊处理
        if rowIndex<=2: return res[rowIndex-1]
        # --------------------------------------
        for ii in range(2,rowIndex):
            for jj in range(1,ii):
                res[ii][jj] = res[ii-1][jj-1]+res[ii-1][jj]
        return res[rowIndex-1]

if __name__ == '__main__':
    s = Solution()
    result = s.getRow(2)
    print(result)
