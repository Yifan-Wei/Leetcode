class Solution:
    from typing import List
    def partition(self, s: str) -> List[List[str]]:
        # 1 <= s.length <= 16
        def is_palindrome(input_s):
            if len(input_s)<=1: return True
            return input_s == input_s[::-1]
        n = len(s)
        res = []
        # map = [[False] * (n) for _ in range(n)]
        # MAP 存储从s[ii:jj+1]的字符串是否是回文, ii=jj时代表单个字符
        # ---------------------------------------------------------
        # for ii in range(n+1):
        #     for jj in range(ii, n):
        #         if is_palindrome(s[ii:jj+1]):
        #             # print(ii,jj, s[ii:jj+1], is_palindrome(s[ii:jj+1]))
        #             map[ii][jj] = True
        # ---------------------------------------------------------
        # for each in map:
        #     print(each)
        # ---------------------------------------------------------
        def dfs(start_p, tmp_plan, answer):
            if start_p >= n:
                answer.append(tmp_plan.copy())
            for ii in range(start_p,n):
                # if map[start_p][ii]:
                if is_palindrome(s[start_p:ii+1]):
                    tmp_plan.append(s[start_p:ii+1])
                    dfs(ii+1, tmp_plan, answer)
                    tmp_plan.pop()

        dfs(0,[],res)
        # for each in res:
        #     print(each)
        return res


if __name__ == '__main__':
    s = Solution()
    result = s.partition("a")
    print(result)
