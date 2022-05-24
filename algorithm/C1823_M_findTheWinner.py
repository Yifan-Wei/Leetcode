class Solution:
    from typing import List
    def findTheWinner(self, n: int, k: int) -> int:
        map = []
        for ii in range(n):
            map.append(ii)
        total = n
        cnt = 0
        p = 0
        while total > 0:
            # print(map, p)
            if p == k-1:
                res = map.pop(cnt)
                total -= 1
            else:
                cnt = (cnt + 1) % len(map)
            p = (p+1) % k
        return res+1




if __name__ == '__main__':
    s = Solution()
    result = s.findTheWinner(5, 2)
    print(result)
