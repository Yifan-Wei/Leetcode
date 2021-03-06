from typing import List
# from collections import defaultdict
class DListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    def insert_after(self, before):
        after = before.next
        self.prev = before
        self.next = after
        before.next = self
        after.prev = self

    def delete_between(self):
        before = self.prev
        after = self.next
        before.next = after
        after.prev = before

    def find_node(self, val):
        p = self
        while p:
            if p.val==val:
                return p
            p = p.next
        return None

    def print_to_the_end(self, iter_max=20):
        list = []
        tmp = self
        iter = 0
        while tmp is not None and iter<=iter_max:
            iter += 1
            list.append(tmp.val)
            tmp = tmp.next
        print(list)

class LRUCache:
    def __init__(self, capacity: int):
        self.INF = 2**31-1
        self.capacity = capacity
        self.total_cache = 0
        self.dummy_head = DListNode(self.INF, self.INF)
        self.dummy_tail = DListNode(self.INF, self.INF)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.cache = {}

    def addToHead(self, node):
        node.insert_after(self.dummy_head)

    def removeNode(self, node):
        node.delete_between()

    def renewNode(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.dummy_tail.prev
        self.removeNode(node)
        return node

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            # RENEW
            target_node = self.cache[key]
            self.renewNode(target_node)
            # self.dummy_head.print_to_the_end()
            # ----------------------------
            return target_node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # ????????????
        if key in self.cache.keys():
            # RENEW
            target_node = self.cache[key]
            self.renewNode(target_node)
            # ????????????: ??????+renew
            target_node.val = value
            # ??????????????????
        else:
            # ??????????????????
            if self.total_cache >= self.capacity:
                # ????????????????????????????????????
                delete_node = self.removeTail()
                # ?????????????????????
                delete_key = delete_node.key
                self.cache.pop(delete_key)
                del delete_node
            else:
                self.total_cache += 1
            # ??????????????????????????????
            add_node = DListNode(key=key, val=value)
            self.addToHead(add_node)
            self.cache[key] = add_node


class QUEUE_LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = []
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.queue:
            index = self.queue.index(key)
            self.queue.pop(index)
            self.queue.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # ??????????????????????????????
        if key in self.queue:
            # ?????????????????????????????????, ????????????????????????????????????
            index = self.queue.index(key)
            self.queue.pop(index)
            self.queue.append(key)
            self.cache[key] = value
        # ??????????????????????????????
        else:
            # ??????????????????, ?????????????????????
            if len(self.queue)==self.capacity:
                out_key = self.queue.pop(0)
                self.cache.pop(out_key)
            self.queue.append(key)
            self.cache[key] = value


if __name__ == '__main__':
    s = LRUCache(1)
    result = s.put(2,1)
    print(s.dummy_head.print_to_the_end())
    result = s.get(2)
    result = s.put(2,2)
    result = s.get(1)
    result = s.get(2)
    result = s.put(1,3)
    print(s.dummy_head.print_to_the_end())
    result = s.put(4,4)
    print(s.dummy_head.print_to_the_end())
    result = s.get(2)
    # print(result)
