class Solution:
    def case1_letterCombinations(self, digits):
        """
        :param digits: str
        :return: List[str]
        """
        n = len(digits)
        if not n:
            return []
        phone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        if n==1:
            return phone[digits[0]]

        def backtrack(conbination, nextdigit):
            if not len(nextdigit):
                ans.append(conbination)
            else:
                for letter in phone[nextdigit[0]]:
                    backtrack(conbination+letter, nextdigit[1:])
        ans = []
        backtrack("", digits)
        return ans

    def letterCombinations(self,digits):
        if not digits: return []
        phone = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        queue = ['']  # 初始化队列, 为第一次弹出的时候做准备
        for digit in digits:
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                for letter in phone[ord(digit) - 50]:  # 这里我们不使用 int() 转换字符串，使用ASCII码
                    queue.append(tmp + letter)
        return queue

if __name__ == "__main__":
    s = Solution()

    result = s.letterCombinations("23")
    print(result) # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    result = s.letterCombinations("")
    print(result)  # []


