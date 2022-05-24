class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗
        # 1 <= s.length, t.length <= 10**5 (这个计算量不像是搜索)
        s_len = len(s)
        t_len = len(t)
        # ------------------------------------
        if t_len > s_len: return ""
        if s == t: return s
        # ------------------------------------
        from collections import defaultdict
        map = defaultdict(int)
        for each in t:
            map[each] += 1
        res = 2 ** 31 - 1
        record = ""
        left_p = 0
        rest_length = t_len
        for ii in range(s_len):
            each = s[ii]
            # 如果符合我的需求, 目标长度减少1
            if map[each]>0:
                rest_length -= 1
            map[each] -=1
            # 目标长度为0时完全匹配, 替代原来的counter_cmp函数
            if rest_length == 0:
                while True:
                    # ---------------------------------
                    remove_char = s[left_p]
                    # 更新最新长度-----------------------
                    now_length = ii - left_p + 1
                    if now_length <= res:
                        record = s[left_p:ii + 1]
                        res = now_length
                    # ----------------------------------
                    # 移除左侧字符-----------------------
                    map[remove_char] = map[remove_char]+1
                    left_p += 1
                    if map[remove_char] > 0:
                        rest_length += 1
                        break
        return record


    def minWindow_answer(self, s: str, t: str) -> str:
        from collections import defaultdict
        need = defaultdict(int)
        for c in t:
            need[c] += 1
        needCnt = len(t)
        i = 0
        res = (0, float('inf'))
        for j, c in enumerate(s):
            if need[c] > 0:
                needCnt -= 1
            need[c] -= 1
            if needCnt == 0:  # 步骤一：滑动窗口包含了所有T元素
                while True:  # 步骤二：增加i，排除多余元素
                    c = s[i]
                    if need[c] == 0:
                        break
                    need[c] += 1
                    i += 1
                if j - i < res[1] - res[0]:  # 记录结果
                    res = (i, j)
                need[s[i]] += 1  # 步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                needCnt += 1
                i += 1
        return '' if res[1] > len(s) else s[res[0]:res[1] + 1]  # 如果res始终没被更新过，代表无满足条件的结果

if __name__ == "__main__":
    s = Solution()
    # result = s.minWindow("a", "aa")
    # print(result)
    result = s.minWindow("ADOBECODEBANCVVVVVVVV","ABC")
    print(result)