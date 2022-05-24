class Solution:
    from typing import List
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def swap(ii,jj):
            tmp = matrix[ii][jj]
            matrix[ii][jj] = matrix[n - jj - 1][ii]
            matrix[n - jj - 1][ii] = matrix[n - ii - 1][n - jj - 1]
            matrix[n - ii - 1][n - jj - 1] = matrix[jj][n - ii - 1]
            matrix[jj][n - ii - 1] = tmp

        n = len(matrix)
        res = n%2
        for ii in range(0, n//2):
            for jj in range(0, n//2):
                swap(ii, jj)
        if res:
            for ii in range(0, n//2):
                jj = n//2
                swap(ii, jj)
        print(matrix)
        return

if __name__ == "__main__":
    s = Solution()
    # s.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
    # s.rotate([[1,2,3,4,5],[6,7,8,9,10],[10,11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
    s.rotate([[1,2,3],[4,5,6],[7,8,9]])