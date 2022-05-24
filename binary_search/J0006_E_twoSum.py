from typing import List


class Solution:
    """
    给定升序数列, 返回两个数值之和等于目标数值的数值下标
    2<=number<=3*10**4
    -1000<=numbers[i]<=1000
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 对任意被搜索数字, numbers[ii], if numbers[ii]>=target/2,下一个数字不可能在他的右侧
        # 换言之左侧的搜索到target/2为止
        n = len(numbers)

        def binary_search(left, right, num_target):
            while left <= right:
                mid = (left+right) >> 1
                if numbers[mid] == num_target:
                    return True, mid
                if numbers[mid] < num_target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False, mid

        for ii in range(n):
            if numbers[ii] > target/2:
                break
            search_res, search_loc = binary_search(ii+1, n-1, target-numbers[ii])
            if search_res:
                return [ii, search_loc]
            else:
                continue
        return -1

if __name__ == '__main__':
    s = Solution()
    result = s.twoSum([1,2,4,6,10],3)
    print(result)
