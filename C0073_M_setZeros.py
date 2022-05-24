class Solution:
    from typing import List
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        height = len(matrix)
        width = len(matrix[0])
        # M+N
        height_list = [1] * height
        width_list = [1] * width
        for ii in range(height):
            for jj in range(width):
                if matrix[ii][jj]==0:
                    height_list[ii] = 0
                    width_list[jj] = 0
        for ii in range(height):
            for jj in range(width):
                if height_list[ii]*width_list[jj]==0:
                    matrix[ii][jj]=0
        print(matrix)
if __name__ == "__main__":
    s = Solution()
    result = s.setZeroes(matrix=[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
    print(result)
