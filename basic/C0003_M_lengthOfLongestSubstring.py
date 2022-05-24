class Solution:
    def case1_lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            result = 0
        else:
            result = 1
        for ii in range(len(s)):
            tmp = s[ii]
            for jj in range(ii+1, len(s)):
                if s[jj] not in tmp:
                    tmp += s[jj]
                    result = max(result, len(tmp))
                else:
                    result = max(result, len(tmp))
                    break
        return result

    def case2_lengthOfLongestSubstring(self, s):
        map = {}
        left = 0
        right = 0
        result = 0
        for ii in range(len(s)):
            now_char = s[ii]
            if left <= right:
                # 如果目前的字符出现在左指针后
                if now_char in map.keys() and map[now_char]>=left:
                    # 发生重复
                    print(s[left:right])
                    result = max(result, right - left)  # 取较大值
                    left = map[now_char] + 1
                    map[now_char] = ii
                else:
                    map[now_char] = ii
            right += 1
        result = max(result, right - left)  # 如果一路都没遇到重复字符, 在这里取最大值
        return result

if __name__ == "__main__":
    s = Solution()
    result = s.case2_lengthOfLongestSubstring("a")
    print(result)