from typing import List

class Solution:
    def exceed_canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # n<=10**5
        n = len(gas)
        gas = gas
        cost = cost
        for ii in range(n):
            # print("出发车站为{0}".format(ii))
            flag = True
            curr_station = ii
            curr_gas = 0
            while (curr_station - ii) < n:
                # 在当前站先加油
                curr_gas += gas[curr_station%n]
                # 从当前站到下一站需要的汽油
                curr_gas -= cost[curr_station%n]
                # print("当前车站为{0}, 加油{1}, 前往下一站需要油{2}, 剩余油{3}".
                      # format(curr_station, gas[curr_station%n], cost[curr_station%n], curr_gas))
                if curr_gas >= 0:
                    curr_station += 1
                else:
                    flag = False
                    break
            if flag:
                # print("当前车站为{0}".format(curr_station))
                return ii
        return -1

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for ii in range(n):
            gas[ii] = gas[ii] - cost[ii]
        if sum(gas) < 0:
            return -1
        ii = 0
        while ii < n:
            if gas[ii] >= 0:
                curr = ii
                total = 0
                flag = True
                while curr < n + ii:
                    total += gas[curr % n]
                    if total >= 0:
                        curr += 1
                    else:
                        ii = curr + 1
                        flag = False
                        break
                if flag:
                    return ii
            else:
                ii += 1
        return -1






if __name__ == '__main__':
    s = Solution()
    result = s.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2])
    # result = s.canCompleteCircuit(gas = [2, 3, 4], cost = [3, 4, 3])
    print(result)
