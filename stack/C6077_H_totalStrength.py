from typing import List


class Solution:
    # 1 <= strength.length <= 10**5
    # 1 <= strength[i] <= 10 ** 9
    def totalStrength(self, strength: List[int]) -> int:
        CONST_PRIME = 10 ** 9 + 7
        n = len(strength)
        psum, ppsum = [0] * n, [0] * n
        # 前缀和与前缀和的前缀和----------------------------------------------
        for ii in range(n):
            if ii:
                psum[ii] = psum[ii-1] + strength[ii]
                ppsum[ii] = ppsum[ii-1] + psum[ii]
            else:
                psum[ii] = strength[ii]
                ppsum[ii] = psum[ii]
        # 单调栈-------------------------------------------------------------
        # strength[ii]作为最小值的管辖范围left[ii]+1~right[ii]-1
        left, right, stack = [-1] * n, [n] * n, []
        for ii in range(n):
            while stack and strength[ii] <= strength[stack[-1]]:
                right[stack.pop()] = ii
            if stack:
                left[ii] = stack[-1]
            stack.append(ii)
        # -------------------------------------------------------------------
        res = 0
        for ii in range(n):
            # Sigma(x=l->i)Sigma(y=i->r) (sum(a[x..y]))
            # = Sigma(x=l->i)Sigma(y=i->r) (psum[y] - psum[x-1])
            # = (ii-l+1) * Sigma(y=i->r)(psum[y]) - (r-ii+1) * Sigma(x=l->i)psum[x-1]
            # = (ii-l+1) * (ppsum[r]-ppsum[i-1]) - (r-ii+1) * (ppsum[i-1] - ppsum[l-2])
            l, r = left[ii]+1, right[ii]-1
            add1 = ppsum[r] if r>=0 else 0
            add2 = -ppsum[ii-1] if ii>=1 else 0
            add3 = -add2
            add4 = -ppsum[l-2] if l>=2 else 0
            multi2 = (ii-l+1) * (add1 + add2) - (r-ii+1) * (add3 + add4)
            # print(strength[ii], "l:{0}, r:{1}, {2}*{3}={4}".format(l,r,strength[ii],multi2,strength[ii]*multi2))
            # print(add1, add2, add3, add4)
            res += strength[ii] * multi2
        res %= CONST_PRIME
        return res

if __name__ == '__main__':
    s = Solution()
    result = s.totalStrength([1,3,1,2])
    # result = s.totalStrength(strength = [747,812,112,1230,1426,1477,1388,976,849,1431,1885,1845,1070,1980,280,1075,232,1330,1868,1696,1361,1822,524,1899,1904,538,731,985,279,1608,1558,930,1232,1497,875,1850,1173,805,1720,33,233,330,1429,1688,281,362,1963,927,1688,256,1594,1823,743,553,1633,1898,1101,1278,717,522,1926,1451,119,1283,1016,194,780,1436,1233,710,1608,523,874,1779,1822,134,1984])
    print(result)
