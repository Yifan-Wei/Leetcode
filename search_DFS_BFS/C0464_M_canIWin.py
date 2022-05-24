from typing import List
from functools import lru_cache
FIRST_ROUND = 0
SECOND_ROUND = 1

class Solution:
    # 1 <= maxChoosableInteger <= 20
    # 0 <= desiredTotal <= 300
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # 状态压缩DP 或者记忆化搜索DFS
        # 极端跳出情况
        n, total = maxChoosableInteger, desiredTotal
        if (((n + 1) * n) >> 1) < total: return False
        # ----------------------------------------------------------------
        # f[mask] 表示初始mask下, 我方先手是否必胜
        f = [False] *(1<<n) # 2**n 状态
        # situ = [1] * (n+1)
        for mask in range((1<<n)-1, -1, -1):
            # 这里的mask相当于一个使用情况表 (mask>>ii)&1 即代表第ii位置有(1)无(0)使用过
            sumOfMask = 0
            for ii in range(n):
                if ((mask >> ii) & 1) > 0:
                    sumOfMask += (ii+1)
            if sumOfMask >= total:
                f[mask] = True
                continue
            for ii in range(n):
                # 这里的状态只可能从 1"0"11111->1"1"11111, 由于是倒序, 显然后者已经先完成遍历了
                # 这里的状态记录了当前情形下是否必胜, 则not(situ)代表该状态必败, 如果能将状态推入下一个状态不能必胜则必胜
                if (mask >> ii) & 1 == 0:
                    if (sumOfMask + (ii+1) >= total) or not(f[mask|1<<ii]):
                        f[mask] = True
        return f[0]

    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @lru_cache(None)
        def dfs(state: int) -> bool:
            cur = sum(i + 1 for i in range(maxChoosableInteger) if state & 1 << i)
            for i in range(maxChoosableInteger):
                if not 1 << i & state and (cur + i + 1 >= desiredTotal or not dfs(state | 1 << i)):
                    return True
            return False

        return (maxChoosableInteger + 1) * maxChoosableInteger // 2 >= desiredTotal and dfs(0)


        # def dfs(map, record, nowTotal, targetTotal, turn):
        #     # print(nowTotal, targetTotal, turn)
        #     n = len(map)
        #     if record == [9, 4]:
        #         print("HERE")
        #     if nowTotal and nowTotal >= targetTotal:
        #         print((turn+1)%2+1, "win")
        #         print(record)
        #         return (turn+1) % 2
        #     for ii in range(n-1, 0, -1):
        #         if map[ii]:
        #             map[ii] = 0
        #             record.append(ii)
        #             tmp = dfs(map, record, nowTotal+ii, targetTotal, (turn+1) % 2)
        #             record.pop()
        #             map[ii] = 1
        #             # 尝试中任意有一次当局获胜则获胜
        #             if tmp == turn:
        #                 print(record, "GO WIN")
        #                 return turn
        #     # 走到这里说明赢不了？
        #     return (turn+1) % 2
        #
        # res = dfs(situ, record, 0, desiredTotal, FIRST_ROUND)
        # return True if not res else False

if __name__ == '__main__':
    s = Solution()
    result = s.canIWin(20, 210)
    # 50/21 = 2 .... 8
    # FIR = 8
    # total = 42, SEC取13以外任意, FIR取其对即可, 如20->1 total=21
    # SEC取13则 TAR=29//21==1....8

    print(result)
