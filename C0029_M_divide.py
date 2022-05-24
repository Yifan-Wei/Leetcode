class Solution:
    """
    给定两个整数，被除数dividend和除数divisor。将两数相除，要求不使用乘法、除法和mod运算符。
    返回被除数dividend除以除数divisor得到的商。
    整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8
    以及
    truncate(-2.7335) = -2
    """
    def divide(self, dividend: int, divisor: int):
        """
        :param  dividend:
        :param  divisor:
        :return:  -> int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # 考虑被除数为最小值的情况 (溢出)
        if dividend == INT_MIN:
            if divisor == 1:
                return INT_MIN
            if divisor == -1:
                return INT_MAX

        # 考虑除数为最小值的情况
        if divisor == INT_MIN:
            if dividend == INT_MIN:
                return 1
            else:
                return 0

        # 一般情况，使用二分查找
        # 将所有的正数取相反数，这样就只需要考虑一种情况
        rev = False
        if dividend > 0:
            dividend = -dividend
            rev = not rev
        if divisor > 0:
            divisor = -divisor
            rev = not rev

        # 快速乘
        def quickAdd(y: int, z: int, x: int):
            """
            :param y:  x 和 y 是负数，z 是正数
            :param z:
            :param x:
            :return: 需要判断 z * y >= x 是否成立 Boolean
            """
            result, add = 0, y
            while z > 0:
                if (z & 1) == 1:
                    # 需要保证 result + add >= x
                    if result < x - add:
                        return False
                    result += add
                if z != 1:
                    # 需要保证 add + add >= x
                    if add < x - add:
                        return False
                    add += add
                # 不能使用除法
                z >>= 1
            return True

        left, right, ans = 1, INT_MAX, 0
        while left <= right:
            # 注意溢出，并且不能使用除法
            mid = left + ((right - left) >> 1)
            check = quickAdd(divisor, mid, dividend)
            if check:
                ans = mid
                # 注意溢出
                if mid == INT_MAX:
                    break
                left = mid + 1
            else:
                right = mid - 1

        return -ans if rev else ans


if __name__ == "__main__":
    # RUN
    s = Solution()
    result = s.divide(242, 5)
    print(result)