class Solution:
    from typing import List
    def exist(self, board: List[List[str]], word: str) -> bool:
        height, width = len(board), len(board[0])
        board_map = [[0]*width for _ in range(height)]
        # print(width, height)
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(xx,yy,size):
            # 正常跳出处理
            if size == len(word):
                print(board_map)
                return True
            # 超出处理
            if xx<0 or xx>=width or yy<0 or yy>=height or board[yy][xx]!=word[size]:
                return False

            if board_map[yy][xx]==0:
                board_map[yy][xx] = 1
                if dfs(xx+1, yy, size+1) or dfs(xx,yy+1,size+1) or dfs(xx-1,yy,size+1) or dfs(xx,yy-1,size+1):
                    return True
                board_map[yy][xx] = 0

        for ii in range(width):
            for jj in range(height):
                if dfs(ii,jj,0):
                    return True
        return False

if __name__ == "__main__":
    s = Solution()
    # result = s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "EEDASFCSE")
    # result = s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE")
    # result = s.exist(board =[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")
    #"""
    result = s.exist(board=[["A","A","A","A","A","A"],
                            ["A","A","A","A","A","A"],
                            ["A","A","A","A","A","A"],
                            ["A","A","A","A","A","A"],
                            ["A","A","A","A","A","A"],
                            ["A","A","A","A","A","A"]], word="AAAAAAAAAAAAAAABA")
    #"""
    print(result)