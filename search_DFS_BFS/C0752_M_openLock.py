class Solution:
    from typing import List
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        「双向 BFS」的基本实现思路如下：
        创建「两个队列」分别用于两个方向的搜索；
        创建「两个哈希表」用于「解决相同节点重复搜索」和「记录转换次数」；
        为了尽可能让两个搜索方向“平均”，每次从队列中取值进行扩展时，先判断哪个队列容量较少；
        如果在搜索过程中「搜索到对方搜索过的节点」，说明找到了最短路径。
        """

        start = "0000"
        # ---------------------------------------------------------------
        if start == target:
            return 0
        if (start in deadends) or (target in deadends):
            return -1
        # ----------------------------------------------------------------

        def both_head_bfs():
            # 「双向 BFS」基本思路对应的伪代码大致如下：
            # d1、d2 为两个方向的队列, m1、m2 为两个方向的哈希表，记录每个节点距离起点的
            # // 只有两个队列都不空，才有必要继续往下搜索
            # // 如果其中一个队列空了，说明从某个方向搜到底都搜不到该方向的目标节点
            # while(!d1.isEmpty() && !d2.isEmpty()) {
            #     if (d1.size() < d2.size()) {
            #         update(d1, m1, m2);
            #     } else {
            #         update(d2, m2, m1);
            #     }
            # }
            from collections import defaultdict
            queue_s_t, queue_t_s = [], []
            hashmap_s_t, hashmap_t_s = defaultdict(), defaultdict()
            queue_s_t.append(start)
            queue_t_s.append(target)
            hashmap_s_t[start] = 0
            hashmap_t_s[target] = 0

            while queue_s_t and queue_t_s:
                t = -1
                if len(queue_s_t)<=len(queue_t_s):
                    t = update(queue_s_t, hashmap_s_t, hashmap_t_s)
                else:
                    t = update(queue_t_s, hashmap_t_s, hashmap_s_t)
                # 搜索终点
                if t!=-1:
                    return t
            # 搜索完成（搜索失败）
            return -1

        def update(queue, hashmap_curr, hashmap_other):
            # // update 为将当前队列 d 中包含的元素取出，进行「一次完整扩展」的逻辑（按层拓展）
            # void update(Deque d, Map cur, Map other) {}
            n = len(queue)
            while n > 0:
                each = queue.pop(0)
                step = hashmap_curr[each]
                for ii in range(4):
                    char = each[ii]
                    # 用-1:2:2的循环来模拟+1和-1
                    for jj in range(-1,2,2):
                        inc_char = str((int(char) + jj) % 10)
                        inc_num = each[0:ii] + inc_char + each[ii + 1:]
                        # --------------------------------------------
                        # print("QUEUE LATER DEAL WITH", inc_num)
                        # --------------------------------------------
                        if inc_num in deadends: continue
                        if inc_num in hashmap_curr: continue
                        # 在另一个哈希表中找到过: 发现最短路径
                        if inc_num in hashmap_other:
                            return step + 1 + hashmap_other[inc_num]
                        else:
                            queue.append(inc_num)
                            hashmap_curr[inc_num] = step + 1
                # ITER
                n -= 1
            return -1

        res = both_head_bfs()
        return res

if __name__ == '__main__':
    s = Solution()
    deadends = ["5557","5553","5575","5535","5755","5355","7555","3555","6655","6455","4655","4455","5665","5445","5645","5465","5566","5544","5564","5546","6565","4545","6545","4565","5656","5454","5654","5456","6556","4554","4556","6554"]
    target = "5555"
    # deadends = ["0201", "0101", "0102", "1212", "2002"]
    # target = "0202"
    # deadends =["8888"]
    # target = "8888"
    # deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    # target = "8888"
    result = s.openLock(deadends, target)
    print(result)
