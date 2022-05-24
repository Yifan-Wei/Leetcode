class Solution:
    from typing import List
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        1 <= num.length <= 10
        -10<=nums[i]<=10
        """
        stack = [[]]
        nums.sort()
        nums_count = {}
        for each in nums:
            if each in nums_count.keys():
                nums_count[each] += 1
            else:
                nums_count[each] = 1
        n = len(nums)
        print(n)
        m_start = 0
        m_end = 1
        iter_num = 0
        tmp = 1  # 记录本组有多少个, 用于下一次循环
        while iter_num<=n:
            print(m_start, m_end)
            for jj in range(m_start, m_end):
                print("------------------------------")
                for ii in range(n):
                    if (ii==0 or nums[ii] != nums[ii-1]) and (len(stack[jj])==0 or nums[ii] >= stack[jj][-1]):
                        if stack[jj].count(nums[ii]) < nums_count[nums[ii]]:
                            ans = stack[jj].copy()
                            ans.append(nums[ii])
                            stack.append(ans)
                            tmp += 1
            m_start = m_end
            m_end = tmp
            iter_num+=1
            print(iter_num)
        return stack

if __name__ == "__main__":
    s = Solution()
    result = s.subsets([1,2,2])
    print(result)
