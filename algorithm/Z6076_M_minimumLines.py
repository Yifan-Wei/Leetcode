from typing import List
from functools import cmp_to_key

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) <= 1: return 0

        def cmp(loc1, loc2):
            if loc1[0] > loc2[0]:
                return 1
            else:
                return -1

        def threePointInLine(loc1, loc2, loc3):
            if loc1 and loc2 and loc3:
                return (loc2[0] - loc1[0]) * (loc3[1] - loc1[1]) == (loc3[0] - loc1[0]) * (loc2[1] - loc1[1])
            else:
                return True

        stockPrices = sorted(stockPrices, key=cmp_to_key(cmp))
        # print(stockPrices)

        last_one_point = None
        last_two_point = None
        res = 1
        for each in stockPrices:
            if last_one_point and last_two_point:
                # 如果没有三点共线就要增加1
                if not threePointInLine(last_two_point, last_one_point, each):
                    res += 1
            last_two_point = last_one_point
            last_one_point = each

        return res

if __name__ == '__main__':
    s = Solution()
    result = s.minimumLines([[3,4],[1,2],[7,8],[2,3]])
    print(result)
