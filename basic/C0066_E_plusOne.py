class Solution:
    from typing import List
    def plusOne(self, digits: List[int]) -> List[int]:
        add = 0
        add_flag = True
        for ii in range(len(digits)-1,-1,-1):
            tmp = digits[ii] + add
            if add_flag:
                tmp += 1
                add_flag = False
            digits[ii] = tmp % 10
            add = tmp // 10
        if add > 0:
            digits.insert(0, add)
        return digits


if __name__ == "__main__":
    s = Solution()
    result = s.plusOne([9,9,9,9])
    print(result)