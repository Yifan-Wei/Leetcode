from typing import List


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # excel = [[ii*jj for ii in range(1,n+1)] for jj in range(1,m+1)]
        # for each in excel:
        #     print(each)
        # print(excel[m-1][n-1])
        # 二分查找
        left = 1  # 最小数字为1
        right = m*n # 最大数字为m*n
        while left < right:
            # 对于查找中的任意数字mid
            mid = left + (right-left)//2
            # print(mid)
            count = 0
            # 对第ii行而言, 这一行的数字为ii*(1,2,3,...,n), 那么只需要加入mid/ii和n中的最小值
            for ii in range(m):
                tmp = mid//(ii+1)
                if tmp <= 0:
                    break
                count += min(tmp, n)
            # print(left, right, mid, count)
            if count >= k:
                right = mid
            elif count < k:
                left = mid + 1
        return left

if __name__ == '__main__':
    s = Solution()
    result = s.findKthNumber(3,3,5)
    print(result)
