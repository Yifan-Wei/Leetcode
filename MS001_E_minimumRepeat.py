"""
深信服面试题
给出字符串，找到能形成此字符串的最小重复单元
如bacbacba, 其最小重复单元为bac
"""

from typing import List

class Solution:
    def substring(self, s1, s2):
        print(s1, s2)
        n1, n2 = len(s1), len(s2)
        if n2>n1:
            return False
        for ii in range(min(n1,n2)):
            if s1[ii]!=s2[ii]:
                return False
        return True

    def minimumRepeat(self, s):
        n = len(s)
        for ii in range(1,n+1):
            last_segment = None
            flag_find = True
            for x in range(n//ii+1):
                if (x+1)*ii<=n:
                    segment = s[ii*x:ii*(x+1)]
                    # print(segment)
                    if last_segment:
                        if segment != last_segment:
                            flag_find = False
                            break
                    last_segment = segment
                else:
                    segment = s[ii*x:]
                    if not self.substring(last_segment, segment):
                        flag_find = False
            if flag_find:
                return ii

if __name__ == '__main__':
    s = Solution()
    result = s.minimumRepeat(s="abdabdabd")
    print(result)
