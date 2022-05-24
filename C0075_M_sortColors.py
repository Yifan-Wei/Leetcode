class Solution:
    from typing import List
    def sortColors(self, nums: List[int]) -> None:
        """
        给定一个包含红色、白色和蓝色、共n个元素的数组nums，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
        我们使用整数 0、1 和 2 分别表示红色、白色和蓝色。
        必须在不使用库的sort函数的情况下解决这个问题。
        Do not return anything, modify nums in-place instead.
        n<=300
        """
        # 你可以不使用代码库中的排序函数来解决这道题吗？
        # 你能想出一个仅使用常数空间的一趟扫描算法吗？
        n = len(nums)
        p0 = p1 = 0  # 下一个0的位置, 下一个1的位置
        for i in range(n):
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1
        print(nums)

if __name__ == "__main__":
    s = Solution()
    result = s.sortColors([2,0,2,1,1,0])
    print(result)