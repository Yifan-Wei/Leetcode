class Solution:
    def isValid(self, s):
        """
        :param s: string
        :return: bool
        """
        queue = []
        dict = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for c in s:
            if c in dict.keys() and len(queue):
                p = len(queue)-1
                if dict[c] == queue[p]:
                    queue.pop(p)
                else:
                    return False
            else:
                queue.append(c)
        if len(queue):
            return False
        return True

if __name__ == "__main__":
    s = Solution()
    result = s.isValid("(()()())")
    print(result)
    result = s.isValid("([]{}([]))")
    print(result)
    result = s.isValid("]")
    print(result)
    result = s.isValid("()[]{}")
    print(result)
