class Solution:
    from typing import List
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        next_greater_num = [-1]*n
        loc_dict = {}
        stack = []
        for ii in range(n-1,-1,-1):
            # print(stack, ii)
            dut = nums2[ii]
            loc_dict[dut] = ii
            while len(stack)>0 and dut>stack[-1]:
                stack.pop()
                # print(stack)
            if len(stack)!=0:
                next_greater_num[ii] = stack[-1]
            else:
                next_greater_num[ii] = -1
            stack.append(dut)
        # print(next_greater_num)
        res = []
        for each in nums1:
            res.append(next_greater_num[loc_dict[each]])
        return res



if __name__ == '__main__':
    s = Solution()
    # result = s.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2])
    result = s.nextGreaterElement(nums1=[2,4], nums2=[1, 2, 3, 4])
    print(result)
