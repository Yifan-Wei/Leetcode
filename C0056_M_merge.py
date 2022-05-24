class Solution:
    from typing import List
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        map = [0] * (2 * 10 ** 4 + 2)
        min_left, max_right = 10 ** 4, 0
        # print(map)
        for each in intervals:
            left, right = each
            # print(left, right)
            min_left = min(left*2, min_left)
            max_right = max(right*2+1, max_right)
            # 中间部分必然连续
            for ii in range(left*2, right*2+1):
                map[ii] = 1
            print(map[0: max_right+1])

        flag_continue = False
        now_left = min_left
        for ii in range(min_left, max_right + 1):
            if map[ii]:
                if flag_continue:
                    continue
                else:
                    flag_continue = True
                    now_left = ii//2
            else:
                if flag_continue:
                    res.append([now_left, (ii-1)//2])
                    flag_continue = False
                else:
                    continue
        return res
if __name__ == "__main__":
    s = Solution()
    # result = s.merge([[1,3],[2,6],[8,10],[15,18]])
    # result = s.merge([[1, 3], [5, 6], [3, 5]])
    # result = s.merge([[1,4],[5,6]])
    result = s.merge([[1,4],[1,4]])
    print(result)
