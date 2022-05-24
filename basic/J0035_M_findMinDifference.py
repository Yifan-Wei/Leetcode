from typing import List
from collections import defaultdict

class DLinkNode:
    def __init__(self, hour, minute, prev=None, next=None):
        self.hour = hour
        self.minute = minute
        self.prev = prev
        self.next = next

class Solution:
    def __init__(self):
        self.ring_link_list = None
        self.time_map = defaultdict()
        for ii in range(24):
            self.time_map[ii] = None
        self.minDiff = 1440

    def insertIn(self, node, node_before):
        if self.ring_link_list:
            node_next = node_before.next
            node_before.next = node
            node.prev = node_before
            node.next = node_next
            node_next.prev = node
        else:
            self.ring_link_list = node
            node.next = node
            node.prev = node

    def findBefore(self, node):
        # 环形链表中没有元素时跳出----------------
        if not self.ring_link_list:
            self.time_map[node.hour] = node
            return None
        # 对应时间表是否有元素--------------------
        if self.time_map[node.hour]:
            handle_node = self.time_map[node.hour]
            if node.minute < handle_node.minute:
                # 更新
                self.time_map[node.hour] = node
                return handle_node.prev
            else:
                last_node = None
                while node.minute >= handle_node.minute:
                    last_node = handle_node
                    handle_node = handle_node.next
                    # 回环跳出
                    if last_node == handle_node:
                        return last_node
                    # 超出跳出
                    if handle_node.hour!=node.hour:
                        return last_node
                return last_node
        else:
            hour = node.hour
            # print(hour)
            while not self.time_map[hour]:
                hour -= 1
                if hour < 0:
                    hour += 24
            hour_node = self.time_map[hour]
            start_hour_node = hour_node
            while hour_node.next.hour == hour:
                if hour_node.next == start_hour_node:
                    self.time_map[node.hour] = node
                    return hour_node
                hour_node = hour_node.next
            self.time_map[node.hour] = node
            return hour_node

    def renewMinDiff(self, node):
        if node:
            next_node = node.next
            if next_node.hour<node.hour:
                hour_diff = next_node.hour+24-node.hour
            else:
                hour_diff = next_node.hour-node.hour
            minute_diff = hour_diff * 60
            minute_diff += next_node.minute-node.minute
            if minute_diff<0:
                minute_diff += 1440
            self.minDiff = min(self.minDiff, minute_diff)

    def DLinkNode_findMinDifference(self, timePoints: List[str]) -> int:
        # 2<=timePoints <=2*10**4
        minDiff = 24*60
        for each_time in timePoints:
            str_hour, str_minute = each_time.split(":")
            hour, minute = int(str_hour), int(str_minute)
            add_node = DLinkNode(hour, minute)
            before_node = self.findBefore(add_node)
            # if before_node:
            #     print(before_node.hour, before_node.minute)
            # else:
            #     print(before_node)
            self.insertIn(add_node, before_node)
        handle_node = self.ring_link_list
        flag = True
        # print("----------------------------------------------")
        while flag or handle_node is not self.ring_link_list:
            if flag:
                flag = False
            self.renewMinDiff(handle_node)
            # print(handle_node.hour, handle_node.minute)
            handle_node = handle_node.next
            # print(self.minDiff)
        return self.minDiff

    def findMinDifference(self, timePoints):
        n = len(timePoints)
        if n > 1440: return 0
        minDiff = 1440
        new_time_list = [0] * n # 必然小于1440
        for ii, each_time in enumerate(timePoints):
            str_hour, str_minute = each_time.split(":")
            hour, minute = int(str_hour), int(str_minute)
            minute_time = hour*60 + minute
            new_time_list[ii] = minute_time
        new_time_list.sort()
        # print(new_time_list)
        for ii in range(n):
            if ii:
                minDiff = min(minDiff, new_time_list[ii]-new_time_list[ii-1])
            else:
                minDiff = min(minDiff, new_time_list[0]+1440-new_time_list[n-1])
        return minDiff



if __name__ == '__main__':
    s = Solution()
    result = s.findMinDifference(["23:59", "00:12", "00:09", "00:00", "00:05"])
    print(result)
