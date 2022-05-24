"""
给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"

提示：
1 <= s.length <= 1000
s 仅由数字和英文字母组成
"""

class Solution:
    def longestPalindrome(self, s):
        """回文字符串"""
        # 偶数串或者奇数串, 对任何一个串都应该满足:
        # 如果一个串s是回文的, 那么除非s[1:-2]="", 否则它也是回文串
        # 单个字母不是回文串, 回文串的长度要>=2
        # 双指针往内部缩进？
        # 动态规划题目: P(i,j) = P(i-1,j-1)&& s[i]==s[j]
        # 边界条件: P(i,i)=True, P(i,i+1)=(s[i]==s[i+1])
        result = None
        length = len(s)
        max_length = -1
        p = [[False] * length for _ in range(length)] # p[i][j] 表示 s[i..j] 是否是回文串
        # 初始化状态方程
        for L in range(1, length+1):
            # 枚举左边界
            for ii in range(length):
                jj = L + ii - 1  # 计算得到右边界
                if jj >= length:  # 越界跳出
                    break
                # 开始计算
                if s[ii] != s[jj]:  # 如果前后两者不相等
                    p[ii][jj] = False  # 不是回文
                else:
                    if L <= 3:
                        p[ii][jj] = True
                    else:
                        p[ii][jj] = p[ii+1][jj-1]
                #
                if p[ii][jj] and L > max_length:
                    # print(ii, jj, L)
                    max_length = L
                    result = s[ii:jj+1]
        return result

if __name__ == "__main__":
    s = Solution()
    result = s.longestPalindrome("ymgkhlrxcabgwziguqjfjqfbfoacyywccbbofqyvmutocnqdrdjpjpvkmhadghbmjgtrafaxgwjfausrurxsfoazyuidvtwavwtojuktafoqzhrofcyvubdnqgmrktuesieqfhcohflyrgwtrtxqvkelyyzrgbltcesqhlvadmdztpkhaqrbhnvekebzkbjtpyuyrzppahembgczswkzbifukzwslsyxngwumeimuvtgkrrvvhbmbgtjymgbvaoebswgkruzgjenucrxxzldeifuqshjnyhcahzsjalqenojbxtnohfdrxozrtclqesuyyerthwbvfrmrprxnevbtqhsxufkxrcgexixfhtteairjlmqobprxblyqcojhbbxykwudnaanduwkyxbbhjocqylbxrpboqmljriaetthfxixegcrxkfuxshqtbvenxrprmrfvbwhtreyyuseqlctrzoxrdfhontxbjoneqlajszhachynjhsqufiedlzxxrcunejgzurkgwsbeoavbgmyjtgbmbhvvrrkgtvumiemuwgnxyslswzkufibzkwszcgbmehappzryuyptjbkzbekevnhbrqahkptzdmdavlhqsectlbgrzyylekvqxtrtwgrylfhochfqeiseutkrmgqndbuvycforhzqofatkujotwvawtvdiuyzaofsxrursuafjwgxafartgjmbhgdahmkvpjpjdrdqncotumvyqfobbccwyycaofbfqjfjqugizwgbacxrlhkgmy")
    print(result)