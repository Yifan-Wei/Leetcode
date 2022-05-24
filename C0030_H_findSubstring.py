class Solution:
    def case1_findSubstring(self, s: str, words: list) -> list:
        """
        给定一个字符串s和一些 长度相同 的单词words 。找出 s 中恰好可以由words 中所有单词串联形成的子串的起始位置。
        注意子串要与words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑words中单词串联的顺序。
        这个思路其实是找最长子串的, 用于完全匹配小题大做了, 在极端测试里面超时了
        :param s:str
        :param words: List[str]
        :return: List[int]
        """
        def findall(haystack, needle):
            list = []
            index = 0
            while True:
                tmp = haystack.find(needle)
                if tmp != -1:
                    index += tmp
                    list.append(index)
                    haystack = haystack[tmp+1:]
                    index += 1
                else:
                    break
            return list

        word_loc_dict = {}
        word_use_dict = {}
        needle_len = 0
        must_len = 0
        total_len = len(s)
        result_list = []
        # 初始化单词位置表
        for each in words:
            # 获取单词长度(仅一次)
            if needle_len == 0:
                needle_len = len(each)
            must_len += needle_len
            if each not in word_loc_dict:
                word_loc_dict[each] = findall(s, each)
            if each in word_use_dict:
                word_use_dict[each] += 1
            else:
                word_use_dict[each] = 1
        # 主程序开始
        print(word_loc_dict)
        print(word_use_dict)
        print(must_len)
        def find_result(start_loc, end_loc):
            nonlocal result_list
            nonlocal s
            # end_loc 代表下一个开始的loc而非上一个结尾的loc
            if end_loc + needle_len > total_len:
                # 没有办法再找下一个了
                if end_loc-start_loc == must_len: # and start_loc not in result_list:
                    result_list.append(start_loc)
            else:
                # 往后接字符串
                for each in word_use_dict.keys():
                    if word_use_dict[each] and (end_loc in word_loc_dict[each]):
                        word_use_dict[each] = word_use_dict[each] - 1
                        find_result(start_loc, end_loc+needle_len)
                        word_use_dict[each] = word_use_dict[each] + 1
                # 也可以不接直接统计
                if end_loc - start_loc == must_len: # and start_loc not in result_list:
                    result_list.append(start_loc)
                # 推起点
                if start_loc == end_loc and end_loc + needle_len + 1 <= total_len:
                    find_result(end_loc+1, end_loc+1)
        find_result(0, 0)
        return result_list


    def findSubstring(self, s, words):
        from collections import Counter   # 统计列表词频
        if not s or not words:
            return []
        one_word = len(words[0])
        all_len = len(words)*one_word
        n = len(s)
        res = []
        words = Counter(words)
        print(words)
        for ii in range(0, n-all_len+1):
            tmp = s[ii:ii+all_len]                  # 截取出来的待匹配字符串
            c_tmp = []
            for jj in range(0, all_len, one_word):
                c_tmp.append(tmp[jj:jj+one_word])   # 把截取出的字符串one_word一组的去匹配
            if Counter(c_tmp) == words:             # 匹配成功, 是一组解
                res.append(ii)
        return res

if __name__ == "__main__":
    a = Solution()
    result = a.findSubstring(s="wordgoodgoodgoodbestword",
                             words=["word", "good", "best", "good"])
    print(result)
    # result = a.findSubstring(s="ababababab",
    #                          words=["ababa", "babab"])
    # print(result)
    # result = s.findSubstring(s="barfoofoobarthefoobarman",
    #                          words=["bar", "foo", "the"])
    # print(result)
    # result = s.findSubstring(s="wordgoodgoodgoodbestword",
    #                          words=["word", "good", "best", "word"])
    # print(result)