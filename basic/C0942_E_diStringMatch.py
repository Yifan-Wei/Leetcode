class Solution:
    from typing import List
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        left = 0
        right = n
        res = []
        for char in s:
            if char=="I":
                res.append(left)
                left += 1
            else:
                res.append(right)
                right -= 1
        res.append(left)
        return res

if __name__ == '__main__':
    s = Solution()
    result = s.diStringMatch("IDID")
    print(result)
