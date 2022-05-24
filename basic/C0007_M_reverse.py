"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围[−2**31, 2**31− 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。
"""
class Solution:
    def case1_reverse(self, x):
        pos_neg = 1
        # 输入为整数, 整数是可以被转换为字符串, 并且至少有1位的
        tmp = str(x)
        neg = "-"
        if tmp.startswith(neg):
            tmp = tmp[1:]
            pos_neg = -1
        # 反转字符串
        tmp = tmp[::-1]
        # 取整数
        ans = pos_neg * int(tmp)
        # 跳出
        max_int = 2**31-1
        min_int = -2**31
        if ans > max_int:
            return 0
        if ans < min_int:
            return 0
        return ans

    def reverse(self, x):
        ans = 0
        max_int = 2 ** 31 - 1
        min_int = 2 ** 31
        max_int_d10 = max_int//10
        min_int_d10 = min_int//10
        neg_pos = 1
        if x<0:
            neg_pos = -1
            x = -x
        while x!=0:
            pop = x % 10
            if neg_pos > 0:
                if ans> max_int_d10 or (ans==max_int_d10 and pop>7):
                    print("up break")
                    return 0
            else:
                if ans>min_int_d10 or (ans==min_int_d10 and pop >8):
                    print("down break")
                    return 0
            ans = ans * 10 + pop
            x = x//10
        return ans*neg_pos


if __name__ == "__main__":
    s = Solution()
    #result = s.reverse(123)
    #print(result)  # 321
    result = s.reverse(-846384741)
    print(result)  # -321
    #result = s.reverse(120)
    #print(result)  # 21
    #result = s.reverse(0)
    #print(result)  # 0
    #result = s.reverse(2147483647)
    #print(result)  # 0