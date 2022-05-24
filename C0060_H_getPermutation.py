class Solution:
    def factorial(self, num: int):
        if num == 0:
            return 1
        else:
            return num * self.factorial(num - 1)

    def getPermutation(self, n: int, k: int) -> str:
        # 1<=n<=9
        res = ""
        num_list = [1] * n
        loc_list = [0] * n
        factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        if k > factorial[n]:
            return -1
        k = k - 1
        for ii in range(n-1, -1, -1):
            tmp = k // factorial[ii]
            loc_list[ii] = tmp
            if tmp>0:
                k -= (tmp*factorial[ii])
        print(loc_list)
        for ii in range(n-1, -1, -1):
            sort_num = loc_list[ii] + 1
            for jj in range(len(num_list)):
                if num_list[jj]>0:
                    sort_num -=1
                if sort_num == 0:
                    res += str(jj+1)
                    num_list[jj] = 0
                    break
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.getPermutation(n=3, k=3)
    print(result)
    result = s.getPermutation(n=3, k=24)
    print(result)