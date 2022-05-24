from typing import List


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        c = ""
        add_last = 0
        for ii in range(max_len-1, -1, -1):
            add_res = int(a[ii]) + int(b[ii]) + add_last
            c = str(add_res % 2)+c
            add_last = add_res//2
        if add_last >0:
            c = str(add_last)+ c
        return c


if __name__ == '__main__':
    s = Solution()
    result = s.addBinary()
    print(result)
