class Solution:
    from typing import List
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if beginWord==endWord: return 1
        if endWord not in wordList: return 0

        def bidirectional_bfs():
            from collections import defaultdict
            # INIT
            # ------------------------------------------------
            queue_b_e, queue_e_b = [], []
            hash_b_e, hash_e_b = defaultdict(), defaultdict()
            queue_b_e.append(beginWord)
            hash_b_e[beginWord] = 0
            queue_e_b.append(endWord)
            hash_e_b[endWord] = 0
            # ------------------------------------------------
            # CORE
            while queue_b_e and queue_e_b:
                t = -1
                # 双向搜索, 优先搜索更短的一边
                if len(queue_b_e)<=len(queue_e_b):
                    t = update(queue_b_e,hash_b_e, hash_e_b)
                else:
                    t = update(queue_e_b,hash_e_b, hash_b_e)
                # 前面的搜索如果成功, 返回结果到t
                if t!=-1:
                    return t
            return -1

        def update(queue:list, hash_curr:dict, hash_other:dict)->int:
            n = len(queue)
            while n>0:
                each = queue.pop(0)
                step = hash_curr[each]
                for word in wordList:
                    # 需要满足: 单词之前没被使用过(否则更短路径到达), 且可以作为后继
                    if word not in hash_curr and valid(each, word):
                        # 已经在另一边找到过, 直接返回对应步数
                        if word in hash_other:
                            return step + 1 + hash_other[word]
                        else:
                            queue.append(word)
                            hash_curr[word] = step + 1
                # ITER
                n -= 1
            return -1

        def valid(word1, word2):
            if len(word1)!= len(word2):
                return False
            tmp = 0
            for ii in range(len(word1)):
                if word1[ii]!=word2[ii]:
                    tmp+=1
                if tmp>1:
                    return False
            if tmp==1:
                return True
            return False

        res = bidirectional_bfs()
        return res + 1

if __name__ == '__main__':
    s = Solution()
    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot", "dot", "dog", "lot", "log"]
    beginWord = "hit"
    endWord = "hit"
    wordList = []
    result = s.ladderLength(beginWord,endWord,wordList)
    print(result)
