from typing import List


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        # 1 <= bottom <= special[i] <= top <= 10**9
        special.append(bottom-1)
        special.append(top+1)
        special.sort()
        # print(special)
        max_len = 0
        for ii in range(len(special)):
            if ii:
                max_len = max(max_len, special[ii]-special[ii-1]-1)
        return max_len

if __name__ == '__main__':
    s = Solution()
    result = s.maxConsecutive(bottom = 6, top = 8, special = [6,7,8])
    print(result)
