from typing import List
from collections import defaultdict, Counter

class Solution:
    # 1 <= s.length, t.length <= 10**5
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m<n: return ""
        # ----------------------------
        map = Counter(t)
        left = -1
        fulfill = 0
        min_len = 2**31-1
        for right in range(m):
            char = s[right]
            # print(s[left + 1:right + 1], fulfill, map)
            if char in map:
                if map[char] > 0:
                    fulfill += 1
                map[char] -= 1
                # print(s[left + 1:right + 1], fulfill, map)
                while fulfill >= n:
                    if right-left<=min_len:
                        res = s[left + 1: right + 1]
                        min_len = right - left
                    left += 1
                    char_out = s[left]
                    if char_out in map:
                        if map[char_out] >= 0:
                            fulfill -= 1
                        map[char_out] += 1
                    # print(s[left+1:right+1], fulfill, map)
        if min_len==2**31-1:
            return ""
        return res





if __name__ == '__main__':
    s = Solution()
    # result = s.minWindow(s="AAAAAAAAAAAAAA", t="ABC")
    # result = s.minWindow(s = "ADOBECODEBANC", t = "ABCC")
    result = s.minWindow(s="abbbbaacaa", t="aaab")
    print(result)
