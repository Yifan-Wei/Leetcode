class Solution:
    from typing import List
    def maxRotateFunction(self, nums: List[int]) -> int:
        # 超时了, 数据量太大, 不能用这种办法
        """n<=10**5"""
        res = -2**32
        n = len(nums)
        if n==1: return 0
        multi_list = [0] * n

        def dot(list1, list2, dim):
            tmp = 0
            for ii in range(dim):
                tmp += list1[ii]*list2[ii]
            return tmp

        for ii in range(n):
            multi_list[ii] = ii
        for ii in range(n):
            # print(dot(multi_list, nums, n))
            res = max(res, dot(multi_list, nums, n))
            pop_num = multi_list.pop(0)
            multi_list.append(pop_num)
        return res

    def maxRotateFunction(self, nums: List[int]) -> int:
        # F(k + 1) = F(k) + sum(nums) - n * nums[-k]
        n, s, f = len(nums), sum(nums), sum(i * num for i, num in enumerate(nums))
        ans = f
        for i in range(1, n):
            f += s - n * nums[-i]
            ans = max(ans, f)
        return ans



if __name__ == "__main__":
    s=Solution()
    result = s.maxRotateFunction([100])
    print(result)