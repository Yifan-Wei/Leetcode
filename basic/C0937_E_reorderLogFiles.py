class Solution:
    from typing import List
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        from functools import cmp_to_key
        digit_list = []
        alpha_list = []

        def cmp(alpha1, alpha2):
            index1, text1 = alpha1.split(" ", 1)
            index2, text2 = alpha2.split(" ", 1)
            # print(index1, text1)
            # print(index2, text2)
            if text1 != text2:
                if text1 > text2:
                    return 1
                else:
                    return -1
            else:
                if index1 >= index2:
                    return 1
                else:
                    return -1

        for each in logs:
            handle_list = each.split(" ")
            if len(handle_list)>1:
                if handle_list[1].isnumeric():
                    digit_list.append(each)
                else:
                    alpha_list.append(each)
            else:
                pass
        """数字信息不需要处理"""
        """字母信息需要重新排序"""
        alpha_list.sort(key=cmp_to_key(cmp))

        return alpha_list + digit_list


if __name__ == '__main__':
    s = Solution()
    # result = s.reorderLogFiles(logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])
    result = s.reorderLogFiles(logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"])
    print(result)
