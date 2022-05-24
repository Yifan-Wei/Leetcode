class Solution:
    from typing import List
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        1 <= n <= 20
        1 <= k <= n
        """
        res = []
        map = [0]*(n+1)
        for ii in range(1,n+1):
            map[ii] = 1
        # print(map)
        stack = []
        def dfs(last, num, map, stack, res):
            if num==0:
                res.append(stack.copy())
            else:
                for ii in range(last, n+1):
                    if map[ii]>0:
                        map[ii] = map[ii]-1
                        stack.append(ii)
                        dfs(ii, num-1, map, stack, res)
                        stack.pop()
                        map[ii] = map[ii]+1

        dfs(1, k, map, stack, res)
        return res

if __name__ == "__main__":
    s = Solution()
    result = s.combine(n=1, k=1)
    print(result)
