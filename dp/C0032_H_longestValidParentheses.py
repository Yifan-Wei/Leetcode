class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 开场剪枝跳出
        if len(s) <2: return 0

        def getElement(input_s: str) -> list:
            tmp_result = []
            queue = []
            order = []
            # Time: O(n) 寻找所有可用子串
            for ii in range(len(s)):
                each = s[ii]
                if each == ")":
                    if len(queue) == 0:
                        continue  # 如果进来的是反括号则无效, 继续往后找
                    else:
                        left, right = order[len(order)-1], ii
                        # print("try add", [left, right])
                        # 长串包裹的短串是没有意义的, 但短串不能被单独获得
                        jj = len(tmp_result)-1
                        while jj >= 0:
                            if tmp_result[jj][0]>left and tmp_result[jj][1]<right:
                                # print(tmp_result)
                                tmp_result.pop(jj)
                            jj -= 1
                        tmp_result.append([left, right])
                        # 退出
                        queue.pop(len(queue)-1)  # 退出一个
                        order.pop(len(order)-1)  # 退出一个
                else:  # 记录左边
                    order.append(ii)
                    queue.append(each)
            print("result = ", tmp_result)
            return tmp_result

        #
        source_list = getElement(s)
        length = len(s)-1
        max_len = 0
        now_len = 0
        p = 0
        while p <= length:
            left_len = length + 1 - p
            if now_len + left_len <= max_len:
                break
            # 贪心就完事了
            find_flag = False
            for each_loc in source_list:
                if each_loc[0] == p:
                    now_len += (each_loc[1]-each_loc[0]+1)
                    p = each_loc[1] + 1
                    find_flag = True
                    break
            if not find_flag:
                max_len = max(now_len, max_len)
                now_len = 0
                p += 1
        max_len = max(now_len, max_len)
        return max_len

    def case2_longestValidParentheses(self, s):
        """
        定义 dp[i]表示以下标i字符结尾的最长有效括号的长度。我们将dp数组全部初始化为0
        有效的子串一定以 ‘)’ 结尾，因此我们可以知道以‘(’ 结尾的子串对应的 dp必定为0
        只需要求解 ‘)’ 在 dp数组中对应位置的值。
        """
        length = len(s)
        if length == 0:
            return 0
        dp = [0] * length
        for i in range(1,length):
            # 当遇到右括号时，尝试向前匹配左括号
            if s[i] == ')':
                pre = i - dp[i-1] - 1
                # 如果是左括号，则更新匹配长度
                if pre>=0 and s[pre] == '(':
                    dp[i] = dp[i-1] + 2
                    # 处理独立的括号对的情形 类似()()、()(())
                    if pre>0:
                        dp[i] += dp[pre-1]
        return max(dp)

    def case3_longestValidParentheses(self, s):
        stack = []
        stack.append(-1)
        max_len = 0
        for ii in range(len(s)):
            if s[ii] == "(":
                stack.append(ii)
                print(stack)
            else:
                stack.pop()
                print(stack)
                if len(stack)==0:
                    stack.append(ii)
                else:
                    max_len = max(max_len, ii-stack[len(stack)-1])
        return max_len




if __name__ == "__main__":
    a = Solution()
    result = a.case3_longestValidParentheses("))()()(()")
    print(result)