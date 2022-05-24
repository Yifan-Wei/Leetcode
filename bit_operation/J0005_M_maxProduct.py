from typing import List
from functools import reduce
from collections import Counter, defaultdict

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0 for _ in range(n)]
        # print(masks)
        for i in range(n):
            for j in range(len(words[i])):
                # ord 返回ASCII码
                ascii_word = ord(words[i][j]) - ord('a')
                bit_list = 1 << ascii_word  # 1<<n = 1*(2**n)
                # 可以理解为生成了一个长度最多为26的二进制列表, 进行或操作时保留对应的位数
                masks[i] |= bit_list
        ans = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    ans = max(len(words[i]) * len(words[j]), ans)
        return ans

    def self_maxProduct(self, words: List[str]) -> int:
        # 2 <= words.length <= 1000
        # 1 <= words[i].length <= 1000
        n = len(words)
        map = defaultdict()
        max_len = 0
        def differ(word_a, word_b):
            for each in map[word_a].keys():
                if each in map[word_b].keys():
                    return False
            return True

        for each in words:
            map[each] = Counter(each)
        for ii in range(n):
            for jj in range(ii, n):
                if differ(words[ii], words[jj]):
                    print(words[ii], words[jj])
                    max_len = max(max_len, len(words[ii]*len(words[jj])))
        return max_len

if __name__ == '__main__':
    s = Solution()
    result = s.maxProduct(["abcw","baz","foo","bar","fxyz","abcdef"])
    # result = s.maxProduct( ["a", "ab", "abc", "d", "cd", "bcd", "abcd"])
    # result = s.maxProduct(["a", "aa", "aaa", "aaaa"])
    print(result)
