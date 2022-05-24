from typing import List
from collections import defaultdict, Counter


class Solution:
    # 1 <= s1.length, s2.length <= 10**4
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 特殊情况返回: 当1长度大于2时不可能是子串-------
        res = []
        s1 = p
        s2 = s
        len1 = len(s1)
        len2 = len(s2)
        if len1 > len2:
            return res
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
            # print(s2[left:right+1])
            # print(map, demand_match_num)
            if demand_match_num==0:
                res.append(left)
        return res

if __name__ == '__main__':
    s = Solution()
    # result = s.findAnagrams(s = "cbaebabacd", p = "abc")
    result = s.findAnagrams(s="abab", p="ab")
    print(result)
