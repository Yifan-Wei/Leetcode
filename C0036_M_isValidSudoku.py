class Solution:
    def is_sub_board_valid(self, board, x, y) -> bool:
        """
        输入任何行列坐标后, 返回此3*3窗格是否有效
        """
        use_list = [0] * 9
        # 先找到3*3窗口的范围
        start_x = (x // 3) * 3
        end_x = start_x + 3
        start_y = (y // 3) * 3
        end_y = start_y + 3
        # print(start_x, start_y)
        for ii in range(start_y, end_y):
            for jj in range(start_x, end_x):
                if board[ii][jj]!=".":
                    tmp = int(board[ii][jj])-1
                    if use_list[tmp] == 0:
                        use_list[tmp] = 1
                    else:
                        # print("False, break")
                        return False
        return True

    def is_col_row_valid(self, board, x, y, col=True):
        use_list = [0] * 9
        if col:
            for ii in range(9):
                if board[ii][x] != ".":
                    tmp_num = int(board[ii][x])-1
                    if use_list[tmp_num] == 0:
                         use_list[tmp_num] = 1
                    else:
                        return False
        else:
            for ii in range(9):
                if board[y][ii] != ".":
                    tmp_num = int(board[y][ii])-1
                    if use_list[tmp_num] == 0:
                        use_list[tmp_num] =1
                    else:
                        return False
        return True

    def isValidSudoku(self, board) -> bool:
        res = True
        # 行列验证
        ii = 0
        while ii < 9:
            res = res and self.is_col_row_valid(board, ii, ii, col=True)
            res = res and self.is_col_row_valid(board, ii, ii, col=False)
            ii += 1
            if not res:
                return False
        # block验证
        for jj in range(0,9,3):
            for ii in range(0,9,3):
                res = res and self.is_sub_board_valid(board, ii, jj)
                if not res:
                    return False
        return True

if __name__ == "__main__":
    s = Solution()
    board =[["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    res = s.isValidSudoku(board=board)
    print(res)
