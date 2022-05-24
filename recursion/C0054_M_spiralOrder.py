class Solution:
    from typing import List
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 将一个大问题转化为小问题
        res = []
        h = len(matrix)
        w = len(matrix[0])
        start_x, end_x = 0, w
        start_y, end_y = 0, h

        while end_x - start_x > 0 and end_y - start_y > 0:
            xx, yy = start_x, start_y
            to_left, to_up = 0, 0
            # right
            for xx in range(start_x, end_x):
                res.append(matrix[yy][xx])
                to_left += 1
            # down
            # print(res)
            for yy in range(start_y + 1, end_y):
                res.append(matrix[yy][xx])
                to_up += 1
            # print(res)
            # left
            if end_y-start_y > 1:
                for xx in range(end_x - 2, start_x - 1, -1):
                    res.append(matrix[yy][xx])
                # print(res)
            # up
            if end_x-start_x > 1:
                for yy in range(end_y - 2, start_y, -1):
                    res.append(matrix[yy][xx])
                # print(res)
            start_x += 1
            end_x -= 1
            start_y += 1
            end_y -= 1
            # print([start_x, end_x], [start_y, end_y])
        return res



if __name__ == "__main__":
    s = Solution()
    result = s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    result = s.spiralOrder([[1,2,3,4,5,6,7]])
    # result = s.spiralOrder([[1,2], [3,4], [5,6], [7,8]])
    print("Result=", result)
    result = s.spiralOrder([[1, 2, 3, 4]])
    # result = s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8]])
    # print("Result=", result)