from typing import List


class Solution:
    def shellSort(self, nums):
        # 时间优于O(N**2), 但不如O(NlogN), 具体取决于使用的增量序列, 空间O(1)
        # 不稳定
        gap = 1
        n = len(nums)
        # 采用Knuth增量序列
        while gap < n // 3:
            gap = gap * 3 - 1
        # 建立在gap上的多次选择排序, gap=1时退化为普通的选择排序
        print("gap=", gap)
        while gap>0:
            print(nums)
            for ii in range(gap, n, gap):
                target = nums[ii]
                jj = ii - gap
                while jj >= 0:
                    print(ii, jj)
                    if target < nums[jj]:
                        nums[jj+gap] = nums[jj]
                        jj -= gap
                    else:
                        break
                if jj != ii-gap:
                    nums[jj+gap] = target
            # 减小gap
            gap //= 3
        print(nums)

if __name__ == '__main__':
    s = Solution()
    result = s.shellSort([1,4,2,8,5,7,9,3,6])
    print(result)
