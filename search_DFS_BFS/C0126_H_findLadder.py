from collections import defaultdict
from collections import deque
from typing import List
import string

class Solution:

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # 先将 wordList 放到哈希表里，便于判断某个单词是否在 wordList 里（效率比list更高?）
        word_set = set(wordList)
        res = []
        # ---------------------------------------------------
        if len(word_set)==0 or endWord not in word_set:
            return res
        # ---------------------------------------------------
        successor = defaultdict(set)
        # step1 使用广度优先遍历得到后继节点表
        found = self.__bfs(beginWord, endWord, word_set, successor)
        if not found:
            return res
        # step2 基于后继节点表, 回溯获得所有最短路径列表
        path = [beginWord]
        print(successor)
        self.__dfs(beginWord, endWord, successor, path, res)
        return res

    def __bfs(self, beginWord, endWord, word_set, successor):
        queue = deque()
        queue.append(beginWord)

        visited = set()
        visited.add(beginWord)

        found = False
        word_len = len(beginWord)
        next_level_visited = set()
        # 大循环
        while queue:
            current_size = len(queue)
            # 层内循环
            for ii in range(current_size):
                current_word = queue.popleft()  # 弹出左侧待处理
                word_list = list(current_word)
                for jj in range(word_len):
                    origin_char = word_list[jj]
                    # 这一步在轮换替代各字符造新词, 并建立对应的链接表-----------
                    for kk in string.ascii_lowercase:
                        word_list[jj] = kk
                        next_word = "".join(word_list)
                        # 新词需要在word set中, 并且不是正在访问中的一个
                        if next_word in word_set and next_word not in visited:
                            if next_word == endWord:
                                found = True
                            # 避免下层元素重复加入队列
                            if next_word not in next_level_visited:
                                next_level_visited.add(next_word)
                                queue.append(next_word)
                            successor[current_word].add(next_word)
                    # 造完归位
                    word_list[jj] = origin_char
                    # -------------------------------------------------------
            if found:
                break
            # 将 next_level_visited 里的所有元素添加到 visited 里, 循环（采用取并集的方法）
            visited |= next_level_visited
            next_level_visited.clear()
        return found

    def __dfs(self, beginWord, endWord, successors, path, res):
        if beginWord == endWord:
            res.append(path[:])
            return

        if beginWord not in successors:
            return

        successor_words = successors[beginWord]
        for next_word in successor_words:
            path.append(next_word)
            self.__dfs(next_word, endWord, successors, path, res)
            path.pop()


if __name__ == '__main__':
    s = Solution()
    result = s.findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"])
    print(result)
