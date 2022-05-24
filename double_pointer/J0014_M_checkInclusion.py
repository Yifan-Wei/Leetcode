from typing import List
from collections import defaultdict, Counter


class Solution:
    # 1 <= s1.length, s2.length <= 10**4
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 特殊情况返回: 当1长度大于2时不可能是子串-------
        len1 = len(s1)
        len2 = len(s2)
        if len1 > len2:
            return False
        # --------------------------------------------
        map = Counter(s1)
        demand_match_num = len1
        left = 0
        for right in range(len2):
            if s2[right] in map.keys():
                if map[s2[right]] > 0:
                    demand_match_num -= 1
                map[s2[right]] -= 1
            if right >= len1:
                if s2[left] in map.keys():
                    if map[s2[left]] >= 0:
                        demand_match_num += 1
                    map[s2[left]] += 1
                left += 1
            print(s2[left:right+1])
            print(map, demand_match_num)
            if demand_match_num==0:
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    result = s.checkInclusion(s1="qff", s2="ifisnoskikfqzrmzlv")
    print(result)
