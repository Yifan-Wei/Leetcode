class Solution:
    from typing import List
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """Word排版单词, 每行最多maxWidth个字符
        1 <= words.length <= 300
        1 <= words[i].length <= 20
        words[i]由小写英文字母和符号组成
        1 <= maxWidth <= 100
        words[i].length <= maxWidth
        """
        res_list = []
        now_length = 0
        to_do_words = []
        # 循环排版处理
        while len(words) > 0:
            each = words[0]
            if now_length + len(each) <= maxWidth:
                words.pop(0)
                to_do_words.append(each)
                now_length = now_length + len(each) + 1
            else:
                res = ""
                n = len(to_do_words)
                res_blank = maxWidth - now_length + n
                if n != 1:
                    min_blank = res_blank // (n-1)
                    rest_blank = res_blank % (n-1)
                    for ii in range(n):
                        res += to_do_words[ii]
                        if ii != n - 1:
                            for _ in range(min_blank):
                                res += " "
                            if rest_blank > 0:
                                res += " "
                                rest_blank -= 1
                else:
                    res += to_do_words[0]
                    while len(res) < maxWidth:
                        res += " "
                res_list.append(res)
                # -------------------
                # 重置为初始状态
                now_length = 0
                to_do_words = []
        # 最后一行打印, 左对齐
        res = ""
        n = len(to_do_words)
        for ii in range(n):
            res += to_do_words[ii]
            if ii != n-1:
                res += " "
        while len(res)<maxWidth:
            res += " "
        res_list.append(res)
        # TEST
        for each in res_list:
            print(len(each))


        return res_list

if __name__ == "__main__":
    s = Solution()
    # result = s.fullJustify(words=["This", "is", "an", "example", "of", "text", "justification."], maxWidth=16)
    result = s.fullJustify(["What","must","be","acknowledgment","shall","be"], maxWidth = 16)
    # result = s.fullJustify(words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20)
    print(result)
