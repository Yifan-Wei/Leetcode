class Solution:
    def binaryGap(self, n: int) -> int:
        n_str = str(bin(n))[2:]
        length = len(n_str)
        max_gap = -1
        last_one = -1
        # print("binary num = ", n_str)
        for ii in range(length):
            if n_str[ii]=="1":
                if last_one >= 0:
                    # print("find none zero gap")
                    max_gap = max(max_gap, ii-last_one)
                # renew
                # print("find 1 in ", ii, "and renewed")
                last_one = ii
        if max_gap <0: return 0
        return max_gap

if __name__ == "__main__":
    s = Solution()
    result = s.binaryGap(22)
    print(result)
