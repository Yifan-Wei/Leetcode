class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")
        res = ""
        stack = []
        for each in path_list:
            if len(each)>0:
                if each == ".":
                    pass
                elif each == "..":
                    if len(stack) > 0:
                        stack.pop()
                else:
                    stack.append(each)
        if len(stack)!=0:
            for ii in range(len(stack)):
                res += ("/"+stack[ii])
        else:
            res = "/"
        return res

if __name__ == "__main__":
    s = Solution()
    result = s.simplifyPath(path="/../")
    print(result)