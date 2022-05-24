class Solution:
    """
    给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
    请你设计并实现时间复杂度为O(n) 的算法解决此问题。
    时间复杂度O(n)
    0 <= nums.length <= 10**5
    -10**9 <= nums[i] <= 10**9
    """
    from typing import List
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        # set不包含重复数字, 去重
        num_set = set(nums)
        print(num_set)

        for num in num_set:
            # 如果不存在比他小1的, 才去找, 否则更小的找的时候就会顺带找到他
            if num-1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num +=1
                    current_streak +=1

                # 挑战最大值
                longest_streak = max(longest_streak, current_streak)

        return longest_streak


if __name__ == '__main__':
    s = Solution()
    result = s.longestConsecutive([100,4,200,1,3,2])
    #result = s.longestConsecutive([2,3,5,100,4])
    #result = s.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
    print(result)
