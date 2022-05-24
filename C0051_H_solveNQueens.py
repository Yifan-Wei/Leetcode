class Solution:
    from typing import List
    def is_place_valid(self, map, xx, yy)->bool:
        n = len(map)
        for ii in range(n):
            if map[xx][ii] == "Q":  # up and down
                return False
            if map[ii][yy] == "Q":  # left and right
                return False
        for ii in range(-n+1, n):
            x_tmp, y_tmp = xx + ii, yy + ii
            if 0 <= (x_tmp) and (x_tmp) < n and 0 <= (y_tmp) and (y_tmp) < n and map[x_tmp][y_tmp] == "Q":
                return False
            x_tmp, y_tmp = xx - ii, yy - ii
            if 0 <= (x_tmp) and (x_tmp) < n and 0 <= (y_tmp) and (y_tmp) < n and map[x_tmp][y_tmp] == "Q":
                return False
            x_tmp, y_tmp = xx + ii, yy - ii
            if 0 <= (x_tmp) and (x_tmp) < n and 0 <= (y_tmp) and (y_tmp) < n and map[x_tmp][y_tmp] == "Q":
                return False
            x_tmp, y_tmp = xx - ii, yy + ii
            if 0 <= (x_tmp) and (x_tmp) < n and 0 <= (y_tmp) and (y_tmp) < n and map[x_tmp][y_tmp] == "Q":
                return False
        return True

    def case1_solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        map = [["."] * n for _ in range(n)]
        col_use_list = [0] * n
        total_quene = n

        def dfsQueens(n, map, use_list, ii, jj, quene, res):
            if quene == 0:
                tmp = []
                for each in map:
                    tmp.append("".join(each))
                res.append(tmp)
                return
            if ii >= n:
                ii = 0
                jj += 1
            if jj >= n:
                return  # 没找到
            # 深搜
            if self.is_place_valid(map, ii, jj):
                map[ii][jj] = "Q"
                dfsQueens(n, map, col_use_list, 0, jj + 1, quene - 1, res)
                map[ii][jj] = "."

            dfsQueens(n, map, col_use_list, ii+1, jj, quene, res)

        dfsQueens(n, map, col_use_list, 0, 0, total_quene, res)

        return res

    def solveNQueens(self, n: int) -> List[List[str]]:
        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def backtrack(row: int):
            if row == n:
                board = generateBoard()
                solutions.append(board)
            else:
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    queens[row] = i
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)

        solutions = list()
        queens = [-1] * n
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        row = ["."] * n
        backtrack(0)
        return len(solutions)


if __name__ == "__main__":
    s = Solution()
    result = s.solveNQueens(9)
    print(result)