"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
例如，121 是回文，而 123 不是。
示例 1：
输入：x = 121
输出：true
示例2：
输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3：
输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。
提示：
-2**31<= x <= 2**31- 1
"""
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            # 负数不回文
            return False
        elif (x<=9) and (x>=0):
            # 个位数必回文
            return True
        else:
            # 大于10的正整数
            tmp = str(x)
            tmp_rev = tmp[::-1]
            if tmp == tmp_rev:
                return True
            else:
                return False

if __name__ == "__main__":
    s = Solution()
    result = s.isPalindrome(-121)
    print(result)