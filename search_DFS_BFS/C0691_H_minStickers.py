from typing import List
from collections import Counter

class Solution:
    # n == stickers.length
    # 1 <= n <= 50 # 最多50个词
    # 1 <= stickers[i].length <= 10  # 每个词长度不超过10
    # 1 <= target <= 15 # 目标长度小于15
    def minStickers(self, stickers, target) -> int:
        # 状态压缩的DP
        sn = len(stickers)
        tn = len(target)
        INF = 2**31-1
        # 统计每个字条字母出现频率
        sticker_char_cnt = [[0 for _ in range(26)] for _ in range(sn)]
        for ii, stick in enumerate(stickers):
            for char in stick:
                sticker_char_cnt[ii][ord(char)-ord("a")] += 1
        # print(sticker_char_cnt)

        # --------- 状压dp 二进制枚举
        dp = [INF for _ in range(1 << tn)]
        dp[0] = 0
        # 实质上这里进行的就是BFS, 因为循环填充入的是sticker中的任意单词, 是每次进入的最小值
        for state in range(0, 1 << tn):
            # 当前状态未完成, 即说明之前通过任何方式无法(由下及上地)到达当前状态
            if dp[state] == INF:
                continue
            # 如果当前状态是之前通过某种方式可以到达的状态, 则循环搜索所有的单词
            for ii in range(sn):
                next_state = state
                char_cnt = sticker_char_cnt[ii].copy()  # 复制一份目标单词表
                # 对每个target的字符进行搜索
                for jj in range(tn):
                    # 如果当前状态表明这个字符已经完成, 则不管
                    if (next_state >> jj) & 1:
                        continue
                    # 如果当前状态的这个字符还未完成, 看新引入的能否完成这个字符

                    if char_cnt[ord(target[jj])-ord("a")]>0:
                        # 假如当前状态为 00000000011(即只有最后两个字符是完成的)
                        # 现在引入的单词 00000000100 能够完成第3个字符
                        # 更新的结果就是 00000000111(为什么不用or呢?)
                        next_state ^= (1<<jj)
                        # 去除1个本次使用的元素
                        char_cnt[ord(target[jj])-ord("a")] -= 1
                # 搜索完成后, 从state完成至新状态next_state
                # 如果next_state未被完成过, 则更新为dp[state]+1, 否则取最小值
                dp[next_state] = min(dp[next_state], dp[state] + 1)
        # 结束的状态为2**n-1对应 11……11, 即每一位都被完成过
        end = (1 << tn) -1
        # 如果重点为INF代表重点没被抵达过, 说明不能完成
        # 否则完成, 返回其结果
        return dp[end] if dp[end]!=INF else -1

    def SELF_minStickers(self, stickers: List[str], target: str) -> int:
        n = len(stickers)
        target_alphabet = [0] * 26
        alphabet = [[0] * 26 for _ in range(n)]
        for char in target:
            target_alphabet[ord(char)-ord("a")] += 1
        for ii in range(n):
            for each_char in stickers[ii]:
                alphabet[ii][ord(each_char)-ord("a")] += 1
        fulfill = len(target)
        min_sticker = 2**31-1
        start_alphabet = [0] * 26

        def combine(now, add_index, tar):
            n = len(now)
            add = alphabet[add_index]
            contribute = 0
            res = now.copy()
            for ii in range(n):
                if add[ii]>0:
                    res[ii] += add[ii]
                    if now[ii]<tar[ii]:
                        contribute += min(tar[ii]-now[ii], add[ii])
            print(stickers[add_index], "contribute", contribute)
            return res, contribute

        for ii in range(n):
            _, contribute = combine(start_alphabet, ii, target_alphabet)
            if contribute<=0:
                print(stickers[ii])

        def dfs(now_sticker, now_alphabet, fulfill_now, last):
            nonlocal min_sticker
            print("====NOW SEARCH {0} sticker: {1}====".format(last, stickers[last]))
            if fulfill_now >= fulfill:
                min_sticker = min(min_sticker, now_sticker)
                return
            for ii in range(last, n):
                # 新增一张ii贴纸
                new_alphabet, contribute = combine(now_alphabet, ii, target_alphabet)
                if contribute > 0:
                    dfs(now_sticker+1, new_alphabet, fulfill_now+contribute, ii)

        # dfs(0, start_alphabet, 0, 0)
        if min_sticker==2**31-1:
            return -1
        return min_sticker

if __name__ == '__main__':
    s = Solution()
    # result = s.minStickers(stickers = ["notice", "possible"], target = "basicbasic")
    result = s.minStickers(stickers = ["with", "example", "science"], target="thehat")
    result = s.minStickers(
    ["control","heart","interest","stream","sentence","soil","wonder","them","month","slip","table","miss","boat","speak","figure","no","perhaps","twenty","throw","rich","capital","save","method","store","meant","life","oil","string","song","food","am","who","fat","if","put","path","come","grow","box","great","word","object","stead","common","fresh","the","operate","where","road","mean"],
        "stoodcrease")
    print(result)
