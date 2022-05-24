import sys
sys.setrecursionlimit(10000)

class Solution:
    from typing import List
    def grayCode_dfs(self, n: int) -> List[int]:

        res = []
        # 图论相关, 连通结构
        # C0/3, C1/3, C2/3, C3/3
        #   1    3      3     1
        #[000,001,011,010,110,111,]
        list_two = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]
        index_list = [[] for _ in range(n + 1)]
        # print(diff_list)
        for ii in range(2**n):
            tmp = str(bin(ii))[2:].zfill(n)
            num = tmp.count("1")
            # diff_list[num].append(tmp)
            index_list[num].append(ii)
        # print(diff_list)
        print(index_list)

        def dfs(num, num_number, res):
            # print(index_list, num)
            # 添加当前值进入结果
            res.append(num)
            # 如果长度抵达, 跳出
            if len(res)==2**n+1:
                print(res)
                return True
            else:
                now_length = num_number
                if now_length < n:
                    next_length = now_length + 1
                    for ii in range(len(index_list[next_length])):
                        next_num = index_list[next_length][ii]
                        if abs(next_num - num) in list_two:
                            # print(next_num, num)
                            # 出列
                            index_list[next_length].pop(ii)
                            # 深搜
                            if not dfs(next_num, next_length, res):
                                # 复原
                                index_list[next_length].insert(ii, next_num)
                            else:
                                return True
                if now_length > 0:
                    next_length = now_length - 1
                    if next_length != 0 or len(res)==2**n:
                        for ii in range(len(index_list[next_length])):
                            next_num = index_list[next_length][ii]
                            if abs(next_num - num) in list_two:
                                # print(next_num, num)
                                # 出列
                                index_list[next_length].pop(ii)
                                # 深搜
                                if not dfs(next_num, next_length, res):
                                    # 复原
                                    index_list[next_length].insert(ii, next_num)
                                else:
                                    return True
            res.pop()
        dfs(0, 0, res)
        return res

    def grayCode(self, n):
        result = ["0","1"]
        res = []
        ii=1
        while ii<n:
            result = result + result[::-1]
            for jj in range(2**ii):
                result[jj] = "0" + result[jj]
            for jj in range(2**ii, 2**(ii+1)):
                result[jj] = "1" + result[jj]
            ii+=1
        for each in result:
            res.append(int(each,2))
        return res

if __name__ == '__main__':
    s = Solution()
    result = s.grayCode(2)
    print(result)

