class Solution:
    def add(self, str1, str2):
        if str1=="0":
            return str2
        if str2=="0":
            return str1
        res = ""
        n1 = len(str1)
        n2 = len(str2)
        n = max(n1, n2)
        if n1 >= n2:
            str2 = "0" * (n1 - n2) + str2
        else:
            str1 = "0" * (n2 - n1) + str1
        extra = 0
        for ii in range(n - 1, -1, -1):
            add_res = int(str1[ii]) + int(str2[ii]) + extra
            extra = add_res // 10
            add_res = add_res % 10
            res = str(add_res) + res
        if extra>0:
            res = str(extra) + res
        return res

    def sub_multiply(self, str1, char2):
        if str1 =="0" or char2=="0":
            return "0"
        res = ""
        n1 = len(str1)
        extra = 0
        for ii in range(n1 - 1, -1, -1):
            mul_res = int(str1[ii]) * int(char2) + extra
            extra = mul_res // 10
            mul_res = mul_res % 10
            res = str(mul_res) + res
        if extra > 0:
            res = str(extra) + res
        return res

    def multiply(self, num1: str, num2: str) -> str:
        """
        给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
        注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。
        """
        if num1 =="0" or num2=="0":
            return "0"
        res = "0"
        n2 = len(num2)
        extra = ""
        for ii in range(n2-1, -1, -1):
            mul_res = self.sub_multiply(num1, num2[ii]) + extra
            extra += "0"
            res = self.add(res, mul_res)
        return res

if __name__ == "__main__":
    s = Solution()
    result = s.multiply("12350", "0")
    print(result)
    print(12350*12078)
