from typing import List
from collections import defaultdict

class Solution:
    # 1 <= words.length <= 100
    # 1 <= words[i].length <= 20
    # order.length == 26 在 words[i]和order中的所有字符都是英文小写字母。
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)
        hash = defaultdict()
        for ii, char in enumerate(order):
            hash[char] = ii
        hash["#"] = -1
        # print(hash)
        def cmp(word1, word2):
            max_len = max(len(word1), len(word2))
            word1 += "#" * (max_len-len(word1))
            word2 += "#" * (max_len-len(word2))
            # print(word1, word2)
            for ii in range(max_len):
                if hash[word1[ii]] < hash[word2[ii]]:
                    return True
                elif hash[word1[ii]] == hash[word2[ii]]:
                    continue
                else:
                    # print(word1[ii], ">", word2[ii])
                    return False
            return True

        for ii in range(n):
            if ii:
                if cmp(words[ii-1], words[ii]):
                    # print(words[ii - 1], "<=", words[ii])
                    continue
                else:
                    # print(words[ii-1], ">", words[ii])
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    # result = s.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz")
    # result = s.isAlienSorted(words = ["world","word","row"], order = "worldabcefghijkmnpqstuvxyz")
    # result = s.isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz")
    print(result)
