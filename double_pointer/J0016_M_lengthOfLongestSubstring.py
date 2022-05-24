from typing import List
from collections import Counter, defaultdict

class Solution:
    # s.length <= 5 * 10**4
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        map_ascii = [0] * 128
        last_pos = [-1] * 128
        n = len(s)
        for right in range(n):
            char = s[right]
            index = ord(char)
            if map_ascii[index]>0:
                char_last_pos = last_pos[index]
                if left < char_last_pos + 1:
                    left = char_last_pos + 1
            else:
                # 这个字符之前没有出现: 更新数目, 更新最新一次的位置
                map_ascii[index] += 1
            # 更新最新出现位置
            last_pos[index] = right
            # 挑战最长串
            # print(s[left:right+1], left, right)
            max_len = max(max_len, right-left+1)
        return max_len

if __name__ == '__main__':
    s = Solution()
    # result = s.lengthOfLongestSubstring("pwwkew")
    # result = s.lengthOfLongestSubstring("abcabcbb")
    result = s.lengthOfLongestSubstring("")
    print(result)
