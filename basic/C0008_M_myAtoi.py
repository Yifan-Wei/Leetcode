"""
请你来实现一个myAtoi(string s)函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。

函数 myAtoi(string s) 的算法如下：
读入字符串并丢弃无用的前导空格
检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
如果整数数超过 32 位有符号整数范围 [−2^31, 2^31− 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被固定为 −231 ，大于 231^− 1 的整数应该被固定为 2^31− 1 。
返回整数作为最终结果。
注意：

本题中的空白字符只包括空格字符 ' ' 。
除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。
"""

class Solution:
    def myAtoi(self, s):
        length = len(s)
        if not length:
            return 0
        sep = " "
        start = -1
        end = -1
        neg_pos = 1
        max_int = 2147483647
        min_int = -2147483648
        p = 0
        end_flag = False
        while not end_flag:
            if start<0:
                if s[p] != sep:
                    if s[p] == "+":
                        neg_pos = 1
                        start = p+1
                    elif s[p] == "-":
                        neg_pos = -1
                        start = p+1
                    elif s[p]<="9" and s[p]>="0":
                        start = p
                    else:
                        return 0
            else:
                if (s[p]<="9" and s[p]>="0"):
                    pass
                else:
                    # 跳出
                    end = p
                    end_flag = True
            p += 1
            # 跳出判断
            if p >= length:
                end = p
                end_flag = True
        # 循环外判断
        if end>start:
            try:
                num = int(s[start:end])
            except:
                num = 0
            tmp = neg_pos * num
            if tmp>max_int:
                tmp = max_int
            elif tmp<min_int:
                tmp = min_int
            return tmp
        else:
            result = 0
        return result

if __name__ == "__main__":
    s = Solution()
    result = s.myAtoi(" -04f")
    # "21474836460"
    # "words and 987"
    print(result)