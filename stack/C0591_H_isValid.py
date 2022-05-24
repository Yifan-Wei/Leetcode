class Solution:
    # def isValid(self, code: str) -> bool:
    #     """591. 标签验证器"""
    #
    #     def isTagMatch(start_match, end_match):
    #         st_match = start_match[1:-1]
    #         ed_match = end_match[2:-1]
    #         # print(st_match, ed_match)
    #         if st_match==ed_match and len(st_match)<=9 and len(st_match)>0:
    #             return True
    #         return False
    #
    #     def deleteCData(input_s:str)->tuple:
    #         import re
    #         # stack = []
    #         tmp_s = input_s
    #         res = ""
    #         while True:
    #             # print("FIND CDATA IN:", tmp_s)
    #             # 寻找CDATA
    #             c_data_start = re.search("<!\[CDATA\[", tmp_s)
    #             # 找不到时跳出
    #             if c_data_start is None:
    #                 res = res + tmp_s
    #                 break
    #             # stack.append(c_data_start)
    #             c_data_end = re.search("\]\]>", tmp_s)
    #             if c_data_end is None:
    #                 # 有开头没结尾, 异常
    #                 return res, False
    #             else:
    #                 # 循环查找
    #                 res = res + tmp_s[:c_data_start.span()[0]]
    #                 # print("RES = ", res)
    #                 # 打印结果-------------------------------------------------
    #                 # c_data = tmp_s[c_data_start.span()[0]:c_data_end.span()[1]]
    #                 # print("C_DATA:", c_data)
    #                 # --------------------------------------------------------
    #                 tmp_s = tmp_s[c_data_end.span()[1]:]
    #         # print("RES = ", res)
    #         return res, True
    #
    #     def isErrorCharExist(input_s:str)->bool:
    #         for each in input_s:
    #             if each=="<":
    #                 return False
    #         return True
    #
    #     def isCodeValid(input_s, first_time=False):
    #         import re
    #         print("-----", input_s,"------")
    #         # 只匹配开头和结尾的合法标签
    #         tmp_s = input_s
    #         stack = []
    #         while True:
    #             start_pattern = re.search("<[A-Z]*>", tmp_s)
    #             if start_pattern is None:
    #                 break
    #             if start_pattern.span()[0]!=0:
    #                 return False
    #             stack.append(start_pattern)
    #
    #
    #
    #             end_pattern = re.search("</[A-Z]*>", tmp_s)
    #
    #
    #
    #
    #         if first_time:
    #             start_pattern = re.search("^<[A-Z]*>", input_s)
    #             end_pattern = re.search("</[A-Z]*>$", input_s)
    #         else:
    #             pass
    #         print(start_pattern, end_pattern)
    #         # 如果被合法标签包围:
    #         if start_pattern and end_pattern:
    #             if isTagMatch(start_pattern.group(), end_pattern.group()):
    #                 if not isCodeValid(input_s[start_pattern.span()[1]:end_pattern.span()[0]]):
    #                     return False
    #             else:
    #                 return False
    #         # 不包含合法标签时:
    #         else:
    #             # 如果是第一次匹配, 第一次匹配必须有合法标签
    #             if first_time:
    #                 # print("FIRST MATCH MUST HAVE HEAD AND TAIL")
    #                 return False
    #             # 如果不是第一次匹配, 不能包含不合法标签和不合法括号
    #             else:
    #                 # print("GET CDATA")
    #                 # 先提取其中的CDATA信息, 摘除后的结果是不包含CDATA的信息
    #                 pure_input_s, is_cdata_valid = deleteCData(input_s)
    #                 if not is_cdata_valid:
    #                     print("CDATA RECOGNIZE ERROR:", input_s)
    #                     return False
    #                 if not isErrorCharExist(pure_input_s):
    #                     print("< or > exist ERROR:", pure_input_s)
    #                     return False
    #         if not first_time and end_pattern is not None:
    #             if not isCodeValid(input_s[end_pattern.span()[1]:]):
    #                 return False
    #         return True
    #
    #     return isCodeValid(code, first_time=True)

    def isValid(self, code: str) -> bool:
        n = len(code)
        tags = list()

        i = 0
        while i < n:
            if code[i] == "<":
                if i == n - 1:
                    return False
                if code[i + 1] == "/":
                    j = code.find(">", i)
                    if j == -1:
                        return False
                    tagname = code[i + 2:j]
                    if not tags or tags[-1] != tagname:
                        return False
                    tags.pop()
                    i = j + 1
                    if not tags and i != n:
                        return False
                elif code[i + 1] == "!":
                    if not tags:
                        return False
                    cdata = code[i + 2:i + 9]
                    if cdata != "[CDATA[":
                        return False
                    j = code.find("]]>", i)
                    if j == -1:
                        return False
                    i = j + 3
                else:
                    j = code.find(">", i)
                    if j == -1:
                        return False
                    tagname = code[i + 1:j]
                    if not 1 <= len(tagname) <= 9 or not all(ch.isupper() for ch in tagname):
                        return False
                    tags.append(tagname)
                    i = j + 1
            else:
                if not tags:
                    return False
                i += 1

        return not tags

if __name__ == '__main__':
    s = Solution()
    # result = s.isValid("<DIV>This is the first line <![CDATA[<div>]]></DIV>")
    # result = s.isValid("<DIV>This is the first line <![CDATA[<div>]]></DIV>>")
    # result = s.isValid("<DIV>This is the first line <![CDATA[<div>]]></DIV></DIV>")
    # result = s.isValid("<DIV>This is the first line <![CDATA[<div>]]></DIV><DIV></DIV>")
    # result = s.isValid("<AV><DIV>This is the first line</DIV></AV>")
    result = s.isValid("<A><A>456</A>  <A> 123  !!  <![CDATA[]]>  123 </A>   <A>123</A></A>")
    print(result)
