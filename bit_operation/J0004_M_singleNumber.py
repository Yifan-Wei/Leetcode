from typing import List


class Solution:
    def singleNumber(self, nums):
        ans = 0
        for i in range(32):
            # num移动i位&1, 判断num的第i位置是否是1
            total = sum((num >> i) & 1 for num in nums)
            # total取3的余数
            if total % 3:
                # Python 这里对于最高位需要特殊判断
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans

    def bit_op_singleNumber(self, nums: List[int]) -> int:
        # 大体的框架思路是, 构造一种位运算方法
        # 位运算方法作用于整个数列之后, 出现三次的数都抵消, 只剩下出现1次的数
        # 比如异或就用来解决2个数的问题
        # 真值表如下:
        # a,b -> x -> a,b
        # 0,0 -> 0 -> 0,0
        # 0,0 -> 1 -> 0,1
        # 0,1 -> 0 -> 0,1
        # 0,1 -> 1 -> 1,0
        # 1,0 -> 0 -> 1,0
        # 1,0 -> 1 -> 0,0
        a, b = 0, 0
        for x in nums:
            a, b = (b & x & (~a)) | (a & (~b) & (~x)),\
                   ((~a) & (~b) & x) | ((~a) & (~x) & b)
            print(a, b)
        return b

if __name__ == '__main__':
    s = Solution()
    result = s.singleNumber([-2,-2,1,1,4,1,4,4,-4,-2])
    # result = s.singleNumber([4, 2, 2, 3, 2, 4, 4])
    print(result)
