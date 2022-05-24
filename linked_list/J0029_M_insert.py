from typing import List
from C0000_ClassListNode import *

class Solution:
    # 给定的可以是这个列表中任意一个顶点的指针，并不一定是这个列表中最小元素的指针。
    # 如果有多个满足条件的插入位置，可以选择任意一个位置插入新的值，插入后整个列表仍然保持有序。
    # 0 <= Number of Nodes <= 5 * 10 ^ 4
    def insert(self, head, insertVal: int):
        # 0节点 --------------------------------------
        if not head:
            res = Node(val=insertVal)
            res.next = res
            return res
        p = head
        first_flag = True
        while True:
            if (p.val<=insertVal and insertVal<=p.next.val) or (p.val > p.next.val and (insertVal > p.val or insertVal < p.next.val)):
                insertNode = Node(val=insertVal)
                tmp = p.next
                p.next = insertNode
                insertNode.next = tmp
                break
            # 如果到了头都没找到好的位置, 说明插入值不满足条件, 随便插入就好
            if p==head:
                if first_flag:
                    first_flag = False
                else:
                    insertNode = Node(val=insertVal)
                    tmp = p.next
                    p.next = insertNode
                    insertNode.next = tmp
                    break
            p = p.next
        return head

if __name__ == '__main__':
    s = Solution()
    input_node = generateNode([1,3,5])
    if input_node:
        input_node.find_tail().next = input_node
    result = s.insert(input_node, 7)
    if result:
        result.print_to_the_end(15)
    print(result)
