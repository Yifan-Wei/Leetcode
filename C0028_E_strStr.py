class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 空寻找直接返回0
        if not len(needle):
            return 0
        length = len(haystack)      # 总长度
        tar_length = len(needle)    # 目标长度
        for ii in range(length):
            # 剩余长度小于目标长度, 返回空
            if length - ii < tar_length:
                return -1
            match_flag = True
            for jj in range(tar_length):
                if haystack[ii+jj] != needle[jj]:
                    match_flag = False
                    break
            if match_flag:
                return ii
        return -1

if __name__ == "__main__":
    s = Solution()
    result = s.strStr("hello", "ll")
    print(result)
    result = s.strStr("aaaaa", "bba")
    print(result)
    result = s.strStr("", "")
    print(result)