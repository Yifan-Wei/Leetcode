class Solution:
    def case1_myPow(self, x: float, n: int) -> float:
        """
        -100.0 < x < 100.0
        -231 <= n <= 231-1
        -10**4 <= xn <= 10**4
        核心思想是分治的快速幂: 2**n = (2**2)**(n/2) n为偶数, 如不满足就将n-1使其为偶数
        复杂度是 O(logn)
        """
        # 预处理
        ans = 1
        if not n:
            return ans
        elif n < 0:
            x = 1/x
            n = -n
        while n:
            if n % 2:
                n -= 1
                ans *= x
            else:
                n = n >> 1
                x *= x
        return ans

    def myPow(self, x, n):
        """官方标准答案"""
        def quickMul(N):
            if N==0:
                return 1.0
            y = quickMul(N//2)
            return y*y if N % 2 == 0 else y * y * x
        return quickMul(n) if n>=0 else 1.0/quickMul(-n)

if __name__ == "__main__":
    s = Solution()
    result = s.myPow(0.5, -10)
    print(result)
