from typing import List
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        MAX_NUM = 26
        # 长度不同肯定不是
        if len(s)!=len(t):
            return False
        # 完全相同不是变位词
        if s==t:
            return False
        # ---------------------------------
        map = [[0]*MAX_NUM for _ in range(2)]
        ordA = ord("a")
        # print(map)
        for char in s:
            map[0][ord(char)-ordA] += 1
        for char in t:
            map[1][ord(char)-ordA] += 1
        for ii in range(MAX_NUM):
            if map[0][ii] != map[1][ii]:
                return False
        return True



    def counterIsAnagram(self, s: str, t: str) -> bool:
        # 长度不同肯定不是
        if len(s)!=len(t):
            return False
        # 完全相同不是变位词
        if s==t:
            return False
        # -----------------------------
        s_counter = Counter(s)
        t_counter = Counter(t)
        if s_counter == t_counter:
            return True
        return False




if __name__ == '__main__':
    s = Solution()
    result = s.isAnagram(s = "anagram", t = "nagaram")
    print(result)
