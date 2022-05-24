from typing import List


class Solution:
    def validPalindrome(self, s: str) -> bool:
        # s<=10**5
        # 循环判断

        def isValid(input_s, differ):
            left = 0
            right = len(input_s) - 1
            while differ <= 1 and left <= right:
                if input_s[left] == input_s[right]:
                    left += 1
                    right -= 1
                    continue
                else:
                    try1 = False
                    try2 = False
                    if differ<1 and left+1<=right and input_s[left+1]==input_s[right]:
                        try1 = isValid(input_s[left + 1:right + 1], 1)
                    if differ<1 and left<=right-1 and input_s[left]==input_s[right-1]:
                        try2 = isValid(input_s[left:right], 1)
                    print(input_s[left+1:right+1], try1, input_s[left:right], try2)
                    return try1 or try2
            return True

        return isValid(s, 0)

if __name__ == '__main__':
    s = Solution()
    # result = s.validPalindrome("abac")
    result = s.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga")
    print(result)
