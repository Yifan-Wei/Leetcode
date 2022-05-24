class Solution:
    from typing import List
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """m,n <=100"""
        n, m = len(matrix), len(matrix[0])
        up_n = 0
        down_n = n-1
        left_m = 0
        right_m = m-1
        while up_n < down_n-1:
            mid_n = (up_n+down_n) >> 1
            if matrix[mid_n][0]>target:
                down_n = mid_n-1
            else:
                up_n = mid_n
        # 锁定在两行之内
        if matrix[down_n][0] > target:
            row = up_n
        else:
            row = down_n
        # 列
        # print(matrix[row])
        while left_m < right_m:
            mid_m = (left_m+right_m) >> 1
            # print(left_m, right_m, mid_m)
            if matrix[row][mid_m] > target:
                right_m = mid_m - 1
            else:
                left_m = mid_m + 1
        # print(left_m, right_m)
        if matrix[row][left_m]==target: return True
        if left_m>0 and matrix[row][left_m-1]==target: return True
        return False

if __name__ == "__main__":
    s = Solution()
    result = s.searchMatrix([[1,3,5,6]],4)
    print(result)