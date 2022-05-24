from typing import List
from collections import deque

MOUSE_TURN = 0
CAT_TURN = 1

DRAW = 0
MOUSE_WIN = 1
CAT_WIN = 2


class Solution:
    # 自己写的没有解决问题, 复杂度应该也超了
    def self_unfinished_catMouseGame(self, graph: List[List[int]]) -> int:
        # 3 <= graph.length <= 50
        def consider(cmp, new_case, prio):
            if prio:
                # 老鼠优先
                if cmp == 1 or new_case == 1:
                    return 1       # 老鼠能赢则赢
                if cmp == 2: return new_case  # 老鼠能不输则不输
                if new_case == 2: return cmp  # 老鼠能不输则不输
                return 0
            else:
                if cmp == 2 or new_case == 2:
                    return 2       # 猫能赢则赢
                if cmp == 1: return new_case  # 猫能不输则不输
                if new_case == 1: return cmp  # 猫能不输则不输
                return 0

        def dfs(mouse, cat, visited, prio):
            if prio:
                print("老鼠先", "老鼠在", mouse,"猫在",cat)
            else:
                print("猫先", "老鼠在", mouse, "猫在", cat)
            if mouse == 0:
                print("老鼠赢")
                return 1
            if mouse == cat:
                print("猫赢")
                return 2
            if (mouse, cat, prio) in visited.keys():
                print("重蹈覆辙")
                return visited[(mouse, cat, prio)]
            # 已访问过节点的添加
            visited[(mouse, cat, prio)] = 0
            # True=老鼠动, False猫动
            if prio:
                # 不走就是输
                tmp = 2
                print("老鼠----思考行动-----")
                for each in graph[mouse]:
                    print("老鼠尝试前往", each)
                    tmp = consider(tmp, dfs(each, cat, visited, (not prio)), prio)
                    # if tmp == 1:
                    #     break
                visited[(mouse, cat, prio)] = tmp
                print("老鼠----思考完毕-----", tmp)
            else:
                # 不走就是输
                tmp = 1
                print("猫----思考行动-----")
                for each in graph[cat]:
                    if each != 0:
                        print("猫尝试前往", each)
                        tmp = consider(tmp, dfs(mouse, each, visited, (not prio)), prio)
                        # if tmp == 2:
                        #     break
                print(mouse, cat, prio, tmp)
                visited[(mouse, cat, prio)] = tmp
                print("猫----思考完毕-----", tmp)
            print(visited)
            return tmp
        # return dfs(1, 4, {}, False)
        return dfs(1, 2, {}, True)

    # 最有策略选择:
    # 如果能赢则必须赢
    # 如果所有移动都败则必败
    # 如果不能必胜，但是存在一种方式进入和局则必须和局
    # 动态规划方法判和
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        # degrees存储从任意节点出发时的状态维度
        degrees = [[[0, 0] for _ in range(n)] for _ in range(n)]
        results = [[[0, 0] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(1, n):
                degrees[i][j][MOUSE_TURN] = len(graph[i])
                degrees[i][j][CAT_TURN] = len(graph[j])
        # 猫的维度-出发点
        for y in graph[0]:
            for i in range(n):
                degrees[i][y][CAT_TURN] -= 1
        # 边界初始化: 老鼠和猫赢的状态
        q = deque()
        for j in range(1, n):
            # 不论是在猫还是在老鼠的回合, 老鼠在洞里就赢了
            results[0][j][MOUSE_TURN] = MOUSE_WIN
            results[0][j][CAT_TURN] = MOUSE_WIN
            q.append((0, j, MOUSE_TURN))
            q.append((0, j, CAT_TURN))
        for i in range(1, n):
            # 不论是在猫还是在老鼠的回合, 猫鼠在同一格猫就赢了
            results[i][i][MOUSE_TURN] = CAT_WIN
            results[i][i][CAT_TURN] = CAT_WIN
            q.append((i, i, MOUSE_TURN))
            q.append((i, i, CAT_TURN))
        # 宽度优先搜索
        while q:
            # 拿出队列中的元素, 老鼠, 猫, 优先权, 寻找到对应的结果
            mouse, cat, turn = q.popleft()
            result = results[mouse][cat][turn]
            # 如果当前的移动方是老鼠，则上一轮的移动方是猫，上一轮状态中老鼠所在节点是mouse，猫所在节点可能是graph中的任意一个节点（除了节点0）；
            if turn == MOUSE_TURN:
                # 上一轮是猫的回合, 则回合开始前猫在其他位置
                prevStates = []
                # 猫上一回合从cat来的
                for prev in graph[cat]:
                    prevStates.append((mouse, prev, CAT_TURN))
            else:
                # 如果当前的移动方是猫，则上一轮的移动方是老鼠，上一轮状态中老鼠所在节点可能是graph中的任意一个节点，猫所在节点是cat。
                prevStates = []
                for prev in graph[mouse]:
                    prevStates.append((prev, cat, MOUSE_TURN))
            for prevMouse, prevCat, prevTurn in prevStates:
                if prevCat == 0:
                    continue    # 猫不能出现在洞里
                if results[prevMouse][prevCat][prevTurn] == DRAW:
                    # 只有平局是需要考虑的, 改变平局的可能是: 这一回合有人能赢
                    canWin = ((result == MOUSE_WIN) and (prevTurn == MOUSE_TURN)) or \
                             ((result == CAT_WIN) and (prevTurn == CAT_TURN))
                    if canWin:
                        results[prevMouse][prevCat][prevTurn] = result
                        # 把新的必胜状态加入队列中
                        q.append((prevMouse, prevCat, prevTurn))
                    else:
                        # 降低上一状态的维度
                        degrees[prevMouse][prevCat][prevTurn] -= 1
                        # 为了实现必败状态与必和状态的判断，需要记录每个状态的度
                        # 初始时每个状态的度为当前玩家在当前位置可以移动到的节点数。
                        # 对于老鼠而言，初始的度为老鼠所在的节点的相邻节点数；
                        # 对于猫而言，初始的度为猫所在的节点的相邻且非0节点的节点数。
                        if degrees[prevMouse][prevCat][prevTurn] == 0:
                            if prevTurn == MOUSE_TURN:
                                results[prevMouse][prevCat][prevTurn] = CAT_WIN
                            elif prevTurn == CAT_TURN:
                                results[prevMouse][prevCat][prevTurn] = MOUSE_WIN
                            # 把新的必胜状态加入队列中
                            q.append((prevMouse, prevCat, prevTurn))
                # 对于不是平局的结果, 想必已经计算过了, 也在队列中, 无需在考虑
        return results[1][2][MOUSE_TURN]

if __name__ == '__main__':
    s = Solution()
    result = s.catMouseGame([[5,6],[3,4],[6],[1,4,5],[1,3,5],[0,3,4,6],[0,2,5]])
    # result = s.catMouseGame([[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]])
    # result = s.catMouseGame([[1,3],[0],[3],[0,2]])
    print(result)
