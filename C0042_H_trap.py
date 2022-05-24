class Solution:
    from typing import List
    def trap(self, height: List[int]) -> int:
        """
        :param height:高度表
        :return: 雨水总数
        一个点储存多少雨水取决于两侧高度差, 左侧最高高度和右侧最高高度
        trap[i] = max(min(left_height[i], right_height[i]) - height[i], 0)
        """
        # 边界
        n = len(height)
        if n<=2: return 0
        left_height = [0] * n
        right_height = [0] * n
        for ii in range(n):
            if ii>0:
                left_height[ii] = max(left_height[ii-1], height[ii-1])
            else:
                left_height[ii] = 0
        for ii in range(n-1, -1, -1):
            if ii<n-1:
                right_height[ii] = max(right_height[ii+1], height[ii+1])
            else:
                right_height[ii] = 0
        ans = 0
        for ii in range(n):
            ans += max(min(left_height[ii], right_height[ii]) - height[ii], 0)
        return ans

if __name__ == "__main__":
    s = Solution()
    res = s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print(res) #->6
    # res = s.trap([4,2,0,3,2,5])
    # print(res) #->9