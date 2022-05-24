class Solution:
    from typing import List
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        rows == matrix.length
        cols == matrix[0].length
        1 <= row, cols <= 200
        matrix[i][j] 为 '0' 或 '1'
        :param matrix:
        :return:
        """
        # -------------------------------------------
        height= len(matrix)
        if height>0:
            width= len(matrix[0])
        else:
            return 0
        # print(width, height)
        # -------------------------------------------

        def dfs(xx_st, xx_ed, yy_st, yy_ed, flag):
            # print("x:[{0}:{1}],y:[{2},{3}],flag={4}".format(xx_st, xx_ed, yy_st, yy_ed, flag))
            if xx_st<0 or xx_ed>=width or yy_st<0 or yy_ed>=height:
                # print("EXCEED ERROR")
                return -1
            if flag=="right":
                for ii in range(yy_st, yy_ed+1):
                    if matrix[ii][xx_ed]=="0":
                        # print("NOT MATCH")
                        return -1
            elif flag=="down":
                for jj in range(xx_st, xx_ed+1):
                    if matrix[yy_ed][jj]=="0":
                        # print("NOT MATCH")
                        return -1
            now_area = (xx_ed - xx_st + 1) * (yy_ed - yy_st + 1)
            # print("NOW AREA = ", now_area)
            if flag != "down":
                right_expand = dfs(xx_st, xx_ed + 1, yy_st, yy_ed, "right")
            else:
                right_expand = -1
            down_expand = dfs(xx_st, xx_ed, yy_st, yy_ed + 1, "down")
            return max(now_area, right_expand, down_expand)

        res = 0
        for ii in range(width):
            for jj in range(height):
                expect_max_area = (width-ii) * (height-jj)
                if res<expect_max_area:
                    # print("------------------------------------")
                    # print(res, expect_max_area)
                    res = max(res, dfs(ii, ii, jj, jj, "right"))
        return res

if __name__ == "__main__":
    s = Solution()
    # result = s.maximalRectangle([])
    # print(result)
    # result = s.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
    a = [["1"]*10 for _ in range(15)]
    result = s.maximalRectangle(a)
    print(result)

