from typing import List


class Solution:
    # n == strs.length
    # 1 <= n <= 100
    # 1 <= strs[i].length <= 1000
    def minDeletionSize(self, strs: List[str]) -> int:
        length = len(strs[0])
        n = len(strs)
        res = 0
        for ii in range(length):
            last_char = None
            for jj in range(n):
                # print(last_char, strs[jj][ii])
                if last_char is not None and strs[jj][ii]<last_char:
                    res += 1
                    # print("BREAk")
                    break
                last_char = strs[jj][ii]
        return res

if __name__ == '__main__':
    s = Solution()
    # result = s.minDeletionSize(strs = ["cba","daf","ghi"])
    result = s.minDeletionSize(strs=["abc", "bce", "cae"])
    print(result)
