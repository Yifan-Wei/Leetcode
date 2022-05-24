from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        calculator = {"+": lambda x,y:x+y,
                      "-": lambda x,y:x-y,
                      "*": lambda x,y:x*y,
                      "/": lambda x,y:int(x/y)
                      }

        for each in tokens:
            if each in calculator.keys():
                num2 = stack.pop()
                num1 = stack.pop()
                # print(num1, calculator, num2)
                stack.append(calculator[each](num1, num2))
            else:
                stack.append(int(each))

        return stack[0]




if __name__ == '__main__':
    s = Solution()
    result = s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
    # result = s.evalRPN(["4","13","5","/","+"])
    print(result)
