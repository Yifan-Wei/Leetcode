class Solution:
    def is_sub_board_valid(self, board, x, y) -> bool:
        """
        输入任何行列坐标后, 返回此3*3窗格是否有效
        """
        use_list = [False] * 9
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
                    if not use_list[tmp]:
                        use_list[tmp] = True
        return use_list

    def is_col_row_valid(self, board, x, y, col=True):
        use_list = [False] * 9
        if col:
            for ii in range(9):
                if board[ii][x] != ".":
                    tmp_num = int(board[ii][x])-1
                    if not use_list[tmp_num]:
                         use_list[tmp_num] = True
        else:
            for ii in range(9):
                if board[y][ii] != ".":
                    tmp_num = int(board[y][ii])-1
                    if not use_list[tmp_num]:
                        use_list[tmp_num] = True
        return use_list

    def solveSudoku(self, board):
        self.iterSolveSudoku(board, 0, 0)
        print(board)

    def iterSolveSudoku(self, board, ii, jj):
        if ii>8:
            ii = 0
            jj += 1
        if jj>8:
            return True
        if board[jj][ii]==".":
            use_list_sub = self.is_sub_board_valid(board, ii, jj)
            use_list_col = self.is_col_row_valid(board, ii, jj, col=True)
            use_list_row = self.is_col_row_valid(board, ii, jj, col=False)
            for kk in range(9):
                if (not use_list_sub[kk]) and (not use_list_col[kk]) and (not use_list_row[kk]):
                    board[jj][ii] = str(kk+1)
                    res = self.iterSolveSudoku(board, ii+1, jj)
                    if res:
                        return res
                    board[jj][ii] = "."
        else:
            return self.iterSolveSudoku(board, ii+1, jj)
        return False

if __name__ == "__main__":
    s = Solution()
    board =[["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]]
    res = s.solveSudoku(board=board)
    # print(res)
