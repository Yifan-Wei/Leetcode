class Solution:
    from typing import List
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # ------------------------------------------------------
        # 1 <= m, n <= 200
        height, width = len(board), len(board[0])
        # board[height][width]
        # ------------------------------------------------------
        # 从边界出发, 所以不被替换的都是边界上的O或者间接与边界相连的O

        def dfs(h, w):
            # 超出边界不再搜索
            if h>=height or h<0 or w>=width or w<0:
                return
            if board[h][w] == "O":
                board[h][w] = "#"
                # print("search ({0},{1})={2}, matched".format(h, w, board[h][w]))
            else:
                # print("search ({0},{1})={2}, not match".format(h, w, board[h][w]))
                return
            dfs(h+1, w)
            dfs(h-1, w)
            dfs(h, w+1)
            dfs(h, w-1)

        for ii in range(height):
            dfs(ii, 0)
            dfs(ii, width-1)
        for ii in range(width):
            dfs(0, ii)
            dfs(height-1, ii)
        # for each in board:
        #     print(each)
        for ii in range(height):
            for jj in range(width):
                if board[ii][jj] == "O":
                    board[ii][jj] = "X"
                elif board[ii][jj] == "#":
                    board[ii][jj] = "O"
        # print("----------------------")
        # for each in board:
        #     print(each)

if __name__ == '__main__':
    s = Solution()
    board = [["X","X","X","X","X"],
             ["X","O","O","O","X"],
             ["X","X","X","X","X"],
             ["X","O","O","X","O"]]
    result = s.solve(board)
    print(result)
