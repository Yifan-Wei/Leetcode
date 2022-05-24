class Solution:
    from typing import List
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        1 <= num.length <= 10
        -10<=nums[i]<=10
        """
        stack = [[]]
        nums.sort()
        n = len(nums)
        m_start = 0
        m_end = 1
        iter_num = 0
        tmp = 0  # 记录本组有多少个, 用于下一次循环
        while iter_num<=n:
            for jj in range(m_start, m_end):
                for ii in range(n):
                    if len(stack[jj])==0 or ((nums[ii] not in stack[jj]) and (nums[ii]>stack[jj][-1])):
                        ans = stack[jj].copy()
                        ans.append(nums[ii])
                        stack.append(ans)
                        tmp += 1
            m_start = m_end
            m_end = tmp
            iter_num+=1
        return stack

if __name__ == "__main__":
    s = Solution()
    result = s.subsets([0,1,1,1,2,3,4,5])
    print(result)
