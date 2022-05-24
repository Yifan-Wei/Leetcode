class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        n = n-1
        while n>0:
            res = self.generateIt(res)
            n -= 1
        return res

    def generateIt(self, string):
        n = len(string)
        p = 0
        res = ""
        last = None
        add = 0
        while p<n:
            if string[p] == last:
                add += 1
            else:
                if add!=0:
                    res += str(add)
                    res += str(last)
                last = string[p]
                add = 1
            p+=1
        if add != 0:
            res += str(add)
            res += str(last)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(1))