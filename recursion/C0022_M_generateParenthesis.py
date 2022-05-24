class Solution:
    def generateParenthesis(self, n: int):
        """
        :param n: int
        :return: List[str]
        # 对任何一个节点而言, 可选有2种, "(" -> (n-1) 或者 ")" -> (n不变)
        # 输入的是个变量, 所以循环次数不定
        """
        List = []
        def generate(s:str, n:int, rev:int):
            if not n and not rev:
                List.append(s)
            elif not n and rev > 0:
                generate(s + ")", n, rev - 1)
            else:
                generate(s+"(", n-1, rev+1)
                if rev > 0:
                    generate(s+")", n, rev-1)
        # run
        generate("", n, 0)
        return List

if __name__ == "__main__":
    s = Solution()
    result = s.generateParenthesis(3)
    print(result)