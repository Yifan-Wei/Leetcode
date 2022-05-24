from typing import List


class Solution:
    def SELF_candy(self, ratings: List[int]) -> int:
        # 能跑, 但是占用O(N)空间
        n = len(ratings)
        up_list = [0] * n
        down_list = [0] * n
        for ii in range(n):
            if ii and ratings[ii] > ratings[ii-1]:
                up_list[ii] = up_list[ii-1] + 1
        for ii in range(n-1,-1,-1):
            if ii!=n-1 and ratings[ii] > ratings[ii+1]:
                down_list[ii] = down_list[ii+1] + 1
        for ii in range(n):
            down_list[ii] = max(up_list[ii], down_list[ii]) + 1
        print(down_list)
        return sum(down_list)

    def candy(self, ratings):
        print(ratings)
        n = len(ratings)
        res = 1
        inc, dec, pre = 1, 0, 1
        for ii in range(1,n):
            if ratings[ii] >= ratings[ii-1]:
                dec = 0
                pre = (1 if ratings[ii]==ratings[ii-1] else pre + 1)
                res += pre
                inc = pre
            else:
                dec += 1
                if dec == inc:
                    dec += 1
                res += dec
                pre = 1
            print(ratings[ii], inc, dec, pre)

if __name__ == '__main__':
    s = Solution()
    # result = s.candy([1,2,2])
    # result = s.SELF_candy([4,7,9,8,7,6,5,4,3,2,3,4,5])
    result = s.candy([4, 7, 9, 8, 7, 6, 5, 4, 3, 2, 3, 4, 5])
    print(result)
