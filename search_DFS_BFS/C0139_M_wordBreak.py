from typing import List
from collections import Counter
from functools import lru_cache

class Solution:
    # 1 <= s.length <= 300
    # 1 <= wordDict.length <= 1000
    # 1 <= wordDict[i].length <= 20
    # s和wordDict[i]仅有小写英文字母组成
    # wordDict中的所有字符串互不相同

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        min_len = 2**31-1
        wordDict = set(wordDict)
        # ------
        memory = [[-1] * n for _ in range(n)]
        # -----------------------------------------
        for each in wordDict:
            min_len = min(min_len, len(each))
        min_len -= 1
        # -----------------------------------------
        for key in Counter(s).keys():
            in_flag = False
            for each in wordDict:
                if key in each:
                    in_flag = True
                    break
            if not in_flag:
                return False

        def dfs(l,r):
            if r>=n:
                return False
            if memory[l][r] != -1:
                return memory[l][r]
            # print("SEARCH", s[l:r+1])
            if r==n-1:
                if s[l:r+1] in wordDict:
                    memory[l][r] = 1
                else:
                    memory[l][r] = 0
            else:
                memory[l][r] = (s[l:r+1] in wordDict and dfs(r+1,r+1+min_len)) or dfs(l,r+1)
            return memory[l][r]

        return True if dfs(0, min_len) else False


if __name__ == '__main__':
    s = Solution()
    # result = s.wordBreak(s = "applepenapple", wordDict = ["apple", "pen"])
    result = s.wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"])
    # result = s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
# ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"])
    print(result)
