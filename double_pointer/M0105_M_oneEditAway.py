from typing import List


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        # 字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。
        # 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。
        # -----------------------------------------------------------
        #
        n_first = len(first)
        n_second = len(second)
        # -----------------------------------------------------------
        if first == second: return True
        # -----------------------------------------------------------
        # 长度相差为0时, 有以下情况
        if n_first == n_second:
            # 两者直接相等(0次编辑)
            tmp = 0
            for ii in range(n_first):
                if first[ii] != second[ii]:
                    tmp += 1
                # 两者不相等, 并且区别大于1个字符
                if tmp > 1:
                    return False
            # 两者不相等, 但是只有1个字符的区别
            return True
        # 插入字符、删除字符、替换字符最多改变1个单位长度, 因此长度相差为2以上的不可能通过一次替换完成
        elif abs(n_first - n_second) >= 2:
            return False
        # 长度相差为1, 必须满足去除相差位置之后两者完全相同
        else:
            if n_first > n_second:
                longer = first
                shorter = second
            else:
                longer = second
                shorter = first
            for ii in range(len(longer)):
                tmp_str = longer[:ii]+longer[ii+1:]
                if tmp_str == shorter:
                    return True
            return False





if __name__ == '__main__':
    s = Solution()
    result = s.oneEditAway("pales", "pale")
    print(result)
