from typing import List


class Solution:
    def tilt(self, nums, x):
        n = len(nums)
        head = 0
        tail = n-1
        while head<tail:
            if nums[head]%x==0:
                head+=1
            else:
                tmp = nums[tail]
                nums[tail] = nums[head]
                nums[head] = tmp
                tail -= 1
        return nums


if __name__ == '__main__':
    s = Solution()
    result = s.tilt([1,2,3,4,5,6,7,8,9], 3)
    print(result)
