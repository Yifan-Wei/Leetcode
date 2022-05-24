from typing import List


class NumMatrix:
    # 1 <= m, n <= 200
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.height = len(matrix)
        self.width = len(matrix[0])
        for each in self.matrix:
            print(each)
        print("--------------------------------")
        for ii in range(self.height):
            for jj in range(self.width):
                if jj:
                    matrix[ii][jj] += matrix[ii][jj-1]
        for ii in range(self.height):
            for jj in range(self.width):
                if ii:
                    matrix[ii][jj] += matrix[ii-1][jj]
        for each in self.matrix:
            print(each)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # print("{0} + {1} - {2} - {3}".format(matrix[row2][col2],
        #                                      matrix[row1-1][col1-1],
        #                                      matrix[row2][0],
        #                                      matrix[0][col2])
        #       )
        if row1 == 0 and col1 == 0:
            return matrix[row2][col2]
        elif row1 == 0:
            return matrix[row2][col2] - matrix[row2][col1-1]
        elif col1 == 0:
            return matrix[row2][col2] - matrix[row1 - 1][col2]
        else:
            return matrix[row2][col2] + matrix[row1-1][col1-1] - matrix[row2][col1-1] - matrix[row1-1][col2]



# Your NumMatrix object will be instantiated and called as such:
matrix = [[3, 0, 1, 4, 2],
          [5, 6, 3, 2, 1],
          [1, 2, 0, 1, 5],
          [4, 1, 0, 1, 7],
          [1, 0, 3, 0, 5]
          ]
obj = NumMatrix(matrix)
param_1 = obj.sumRegion(2,1,4,3)
print(param_1)
param_2 = obj.sumRegion(1,1,2,2)
print(param_2)


[1,1,2,2]
