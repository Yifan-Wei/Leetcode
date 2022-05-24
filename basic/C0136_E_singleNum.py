from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash = {}
        for each in nums:
            if each not in hash:
                hash[each]=1
            else:
                hash[each]+=1
        for key in hash.keys():
            if hash[key]==1:
                return key
        # print(hash)

if __name__ == '__main__':
    s = Solution()
    result = s.singleNumber([4,1,2,1,2])
    print(result)
