class Solution:
    def case1_findMedianSortedArrays(self, nums1:list, nums2:list):
        """
        :param nums1: List[int]
        :param nums2: List[int]
        :return:->float
        """
        nums1 += nums2
        nums1.sort()
        if len(nums1)%2:
            medium = len(nums1)//2
            ans = float(nums1[medium])
        else:
            medium = len(nums1)//2-1
            medium2 = medium+1
            ans = float((nums1[medium]+nums1[medium2])/2)
        return ans

if __name__ == "__main__":
    s = Solution()
    result = s.findMedianSortedArrays([1,2,4],[3,4])
    print(result)

