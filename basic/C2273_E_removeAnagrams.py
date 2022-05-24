from typing import List
from collections import Counter

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        if len(words)<=1:
            return words
        word_counter = {}
        for each in words:
            word_counter[each] = Counter(each)
        ii = 1
        while True:
            # print(ii)
            if ii and word_counter[words[ii]]==word_counter[words[ii-1]]:
                words.pop(ii)
                ii -= 1
            ii += 1
            if ii>=len(words):
                return words

if __name__ == '__main__':
    s = Solution()
    result = s.removeAnagrams(words=["abababaab"])
    # result = s.removeAnagrams(words= ["a","b","c","d","e"])
    print(result)
