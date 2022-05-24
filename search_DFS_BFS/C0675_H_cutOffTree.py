from typing import List
from bisect import bisect_right
from functools import cmp_to_key
from collections import deque

class Solution:
    # m == forest.length
    # n == forest[i].length
    # 1 <= m, n <= 50
    # 0 <= forest[i][j] <= 10**9
    # 可以保证没有两棵树的高度是相同的
    def cutOffTree(self, forest: List[List[int]]) -> int:
        MAX_INF = 2**31-1
        m, n = len(forest), len(forest[0])
        stepPre = [(0,1),(1,0),(0,-1),(-1,0)]
        map = []
        # forest[yy:m][xx:n]
        def cmp(tuple1, tuple2):
            if tuple1[0] > tuple2[0]:
                return 1
            else:
                return -1

        res = 0
        for yy in range(m):
            for xx in range(n):
                if forest[yy][xx]>1:
                    map.append((forest[yy][xx], xx, yy))
        map = sorted(map, key=cmp_to_key(cmp))
        map.insert(0, (forest[0][0], 0, 0))
        print(map)
        for ii in range(1, len(map)):
            start_height, start_xx, start_yy = map[ii-1]
            target_height, target_xx, target_yy = map[ii]
            queue = deque()
            queue.append((start_xx, start_yy, 0))
            road = MAX_INF
            hash = {}
            while queue:
                xx, yy, step = queue.popleft()
                if yy>=m or yy<0 or xx>=n or xx<0 or forest[yy][xx]==0:
                    # print("地块:[{0}][{1}]异常, 无法前进".format(xx, yy))
                    continue
                if xx == target_xx and yy == target_yy:
                    road = step
                    print("抵达地块:forest[{0}][{1}]={2}, 共用{3}步".format(target_xx, target_yy, forest[target_yy][target_xx], step))
                    break
                for ii in range(4):
                    if (xx+stepPre[ii][0], yy+stepPre[ii][1]) not in hash.keys():
                        hash[(xx+stepPre[ii][0], yy+stepPre[ii][1])] = step+1
                        queue.append((xx+stepPre[ii][0], yy+stepPre[ii][1], step+1))
            if road==MAX_INF:
                return -1
            else:
                res+=road
        return res



if __name__ == '__main__':
    s = Solution()
    # forest = [[0,1,2]]
    # forest = [[1,2,3],[0,0,4],[7,6,5]]
    forest = [[54581641,64080174,24346381,69107959],
              [86374198,61363882,68783324,79706116],
              [668150,92178815,89819108,94701471],
              [83920491,22724204,46281641,47531096],
              [89078499,18904913,25462145,60813308]]
    # forest = [[1, 2, 3],
    #           [6, 7, 1],
    #           [1, 5, 4]]
    result = s.cutOffTree(forest)
    print(result)
