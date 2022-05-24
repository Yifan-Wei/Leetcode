class Solution:

    def case1_isMatch(self, s: str, p: str) -> bool:
        """
        :param s: 待匹配字符串
        :param p: 包含*和?的通配匹配符
        :return:
        * 包含递归的思想, 当需要匹配*的时候, 实际上需要解决没有*的任意子问题
        如 abcabde
           *bde
        """
        new_p = ""
        for ii in range(len(p)):
            if ii>0 and p[ii]=="*" and p[ii-1]=="*":
                pass
            else:
                new_p += p[ii]
        print(new_p)

        def starMatch(s, p):
            if len(p) == 0:
                if len(s) == 0:
                    return True
                else:
                    return False
            if p[0] == "*":
                res = False
                if len(s)!=0:
                    for ii in range(len(s)):
                        tmp_res = starMatch(s[ii:len(s)], p[1:len(p)])
                        # print(s[ii:len(s)], p[1:len(p)],"MATCH=", tmp_res)
                        res = res or tmp_res
                    tmp_res = starMatch("", p[1:len(p)])
                    res = res or tmp_res
                else:
                    res = starMatch("", p[1:len(p)])
                return res
            else:
                if len(s)!=0:
                    if s[0] == p[0] or p[0]=="?":
                        return starMatch(s[1:len(s)], p[1:len(p)])
                    else:
                        return False
                else:
                    return False

        return starMatch(s, new_p)

    def isMatch(self,s,p):
        """
        :param s:
        :param p:
        :return:
        dp[i][j]表示s[0:i+1]与p[0:j+1]是否能够匹配
        if p[j]=="?":
            dp[i][j] = dp[i-1][j-1]
        elif p[j]=="*":
            dp[i][j] = dp[i][j-1] or dp[i-1][j]
            其中dp[i][j-1]代表跳过*, 即"*"匹配空字符
            而dp[i-1][j]代表使用"*", "*" 匹配当前位置
        else:
            dp[i][j] = dp[i-1][j-1]
        """
        m, n = len(s), len(p)
        dp = [[False]*(len(p)+1) for _ in range(m+1)]
        dp[0][0] = True
        # 只有当剩余字符串全为*时为True
        for ii in range(1, n+1):
            if p[ii-1] == "*":
                dp[0][ii] = True
            else:
                # 只要有一个不为"*"就跳出初始化
                break
        # 从1循环到m, 从1循环到n, 都是匹配位数, 所以要-1
        for ii in range(1, m+1):
            for jj in range(1, n+1):
                if p[jj - 1] == "*":
                    dp[ii][jj] = dp[ii][jj-1] | dp[ii-1][jj]
                elif p[jj - 1] == "?" or s[ii - 1] == p[jj - 1]:
                    dp[ii][jj] = dp[ii-1][jj-1]

        return dp[m][n]



if __name__ == "__main__":
    s = Solution()
    result = s.isMatch("", "*b*")
    result = s.isMatch("acdcb", "*a*b")
    print(result)
    result = s.isMatch("aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba","*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*")
    print(result)


