class Solution:
    def mySqrt(self, x: int) -> int:
        """
        0 <= x <= 2**31 - 1
        返回整数算数平方根的整数部分
        """
        if x==0: return 0
        if x==1 or x==2: return 1

        left = 0
        right = 46340  # (2**31-1)**0.5
        while left<right:
            mid = (left+right) >> 1
            # print(left, right, mid)
            if mid*mid <= x:
                left = mid+1
            else:
                right = mid-1

        if left*left <= x:
            return left
        else:
            return left-1




if __name__ == "__main__":
    s = Solution()
    #result = s.mySqrt(1)
    #result = s.mySqrt(1)
    #result = s.mySqrt(1)
    result = s.mySqrt(28267)
    print(result)