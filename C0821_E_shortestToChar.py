class Solution:
    from typing import List
    def shortestToChar(self, s: str, c: str) -> List[int]:
        right_res = [-1]*len(s)
        left_res = [-1]*len(s)
        res = []
        last_char = -10**5
        for ii in range(len(s)):
            if s[ii] == c:
                right_res[ii] = 0
                last_char = ii
            else:
                right_res[ii] = abs(ii-last_char)
        last_char = 10**5
        for ii in range(len(s)-1, -1, -1):
            if s[ii] == c:
                left_res[ii] = 0
                last_char = ii
            else:
                left_res[ii] = abs(ii-last_char)
        for ii in range(len(s)):
            res.append(min(left_res[ii], right_res[ii]))
        return res

if __name__ == "__main__":
    s = Solution()
    result = s.shortestToChar(s="loveleetcode", c="e")
    print(result)
