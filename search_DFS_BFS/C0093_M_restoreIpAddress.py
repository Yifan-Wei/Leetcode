class Solution:
    from typing import List
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)

        def standard_test(input_s):
            if len(input_s)<=0:
                return False
            if input_s != "0" and input_s[0] == "0":
                return False
            try:
                res_int = int(input_s)
                if res_int>255 or res_int<0:
                    return False
            except Exception as e:
                return False
            return True

        def dfs(length, ans_list, match_string, res):
            # 长度超标直接退出
            if length==n and len(ans_list)==4 and len(match_string)==0:
                tmp = ""
                for each in ans_list:
                    tmp += (each+".")
                res.append(tmp[:-1])
            if length > n:
                return
            if len(ans_list) > 4:
                return
            if standard_test(match_string):
                ans_list.append(match_string)
                dfs(length, ans_list, "", res)
                ans_list.pop()
            if length < n:
                dfs(length+1, ans_list, match_string+s[length], res)

        # 搜索主函数
        dfs(0, [], "", res)
        # res = standard_test("125")
        return res

if __name__ == '__main__':
    s = Solution()
    result = s.restoreIpAddresses("101023")
    print(result)
