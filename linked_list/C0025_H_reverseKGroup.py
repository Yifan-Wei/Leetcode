# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_to_the_end(self):
        list = []
        tmp = self
        while tmp is not None:
            list.append(tmp.val)
            tmp = tmp.next
        print(list)

class Solution:
    # 翻转子链表
    def reverse(self, head, tail):
        """
        链表只需要考虑后缀不需要考虑前序, 因此不断把头部丢到尾部形成新后缀, 当丢到尾部时就完成了
        """
        prev = tail.next        # 尾部连接的后续部分
        p = head                # 头部
        while prev != tail:     # 当尾部没有连接头部时
            nex = p.next        # 下一个元素
            p.next = prev       # 头部直接接尾部
            prev = p            # 尾部是包含头部在内的尾部
            p = nex             # 指针后移
        return tail, head

    def reverseKGroup(self, head, k):
        """
        :param head: Optional[ListNode]
        :param k: int
        :return: Optional[ListNode]
        """
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next

        return hair.next







if __name__ == "__main__":
    # RUN
    s = Solution()

    # case1
    node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    node.print_to_the_end()
    result = s.reverseKGroup(node, 4)
    result.print_to_the_end()

    # case2
    node = ListNode(1, None)
    result = s.reverseKGroup(node, 1)
    result.print_to_the_end()

    # case3
    node = None
    result = s.reverseKGroup(node, 1)
    print(result)
    # result.print_to_the_end
