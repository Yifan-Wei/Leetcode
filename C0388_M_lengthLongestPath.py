class Solution:
    def lengthLongestPath(self, input: str) -> int:
        res = 0
        input_list = input.split("\n")
        print(input_list)
        max_deep = -1
        deep = -1
        root = []

        for each in input_list:
            # 预处理
            tmp = each.split("\t")
            # 获取当前进来的深度
            tmp_deep = len(tmp)-1
            tmp_each = tmp[-1]

            # Root Stack
            if tmp_deep <= deep:
                while len(root) > tmp_deep:
                    root.pop()
            deep = tmp_deep
            root.append(tmp_each)
            print(root, tmp_each)
            # write
            if "." in tmp_each:
                max_deep = tmp_deep
                tmp_ans = ""
                for every_root in root:
                    tmp_ans = tmp_ans + every_root + "\\"
                tmp_ans = tmp_ans[:-1]
                print("max deep renew as:", tmp_ans)
                res = max(res, len(tmp_ans))

        return res


if __name__ == "__main__":
    s = Solution()
    #result = s.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
    #print(result)
    # result = s.lengthLongestPath("file1.txt\nfile2.txt\nlongfile.txt")
    # result = s.lengthLongestPath("dir\n\tsubdir1\n\t\tsubdir2\n\t\t\tsubdir3\na.txt")
    result = s.lengthLongestPath("a\n\taa\n\t\taaa\n\t\t\tfile1.txt\naaaaaaaaaaaaaaaaaaaaa\n\tsth.png")
    print(result)