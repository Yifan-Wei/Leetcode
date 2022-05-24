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
    def mergeTwoLists(self, list1, list2):
        """
        :param list1: Optional[ListNode] 一个升序链表
        :param list2: Optional[ListNode] 一个升序链表
        :return:Optional[ListNode]
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        dummy = ListNode()  # 哑节点
        tmp1 = list1
        tmp2 = list2
        tmp3 = dummy
        while tmp1 is not None and tmp2 is not None:
            if tmp1.val < tmp2.val:
                tmp3.next = tmp1
                tmp1 = tmp1.next
            else:
                tmp3.next = tmp2
                tmp2 = tmp2.next
            tmp3 = tmp3.next
        # 狗尾续貂
        if tmp1 is not None:
            tmp3.next = tmp1
        else:
            tmp3.next = tmp2

        return dummy.next

if __name__ == "__main__":
    node2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    node1 = ListNode(2, ListNode(3, ListNode(4, ListNode(6,None))))
    s = Solution()
    result = s.mergeTwoLists(node1,node2)
    result.print_to_the_end()