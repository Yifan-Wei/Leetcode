class RecentCounter:
    """
    t<=10**9
    ping at most 10**4
    """
    def __init__(self):
        self.quest_list = []

    # def ping(self, t: int) -> int:
    #     self.quest_list.append(t)
    #     back_trace_time = t-3000
    #     quest_num = 0
    #     for ii in range(len(self.quest_list)-1,-1,-1):
    #         if self.quest_list[ii]>= back_trace_time:
    #             quest_num += 1
    #         else:
    #             break
    #     return quest_num

    def ping(self, t: int) -> int:
        self.quest_list.append(t)
        back_trace_time = t-3000
        while self.quest_list[0] < back_trace_time:
            self.quest_list.pop(0)
        return len(self.quest_list)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

if __name__ == '__main__':
    obj = RecentCounter()
    param_1 = obj.ping(1)
    param_2 = obj.ping(100)
    param_3 = obj.ping(3001)
    param_4 = obj.ping(3002)
    print(param_1,param_2,param_3,param_4)
    # print(result)
