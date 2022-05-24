class Solution:
    from typing import List
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        # 将nums2合并入nums1
        # 时间复杂度O(m+n)
        """
        load_p = m+n-1
        find_m = m-1
        find_n = n-1
        while load_p>=0:
            chose1 = nums1[find_m] if find_m>=0 else -1
            chose2 = nums2[find_n] if find_n>=0 else -1
            if chose1>=chose2:
                nums1[load_p] = chose1
                find_m-=1
            else:
                nums1[load_p] = chose2
                find_n-=1
            load_p -= 1
        return

if __name__ == '__main__':
    s = Solution()
    # result = s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    result = s.merge([1,3,4,6,0,0,0,0],4,[2,2,3,5],4)
    print(result)
