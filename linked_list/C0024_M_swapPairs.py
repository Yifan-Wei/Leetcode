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
    def swapPairs(self, head: ListNode):
        """
        给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。
        你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
        链表中节点的数目在范围 [0, 100] 内
        0 <= Node.val <= 100
        :param head: ListNode
        :return: ListNode
        """
        dummy = ListNode()
        node_be_suc = dummy
        node_to_do = head

        while True:
            if node_to_do is not None and node_to_do.next is not None:
                # 在保证待处理节点和下一节点存在时
                first_node = node_to_do             # 待处理节点
                second_node = node_to_do.next       # 下一节点
                third_node = node_to_do.next.next   # 接续节点
                node_be_suc.next = second_node      # 接续第2个节点
                node_be_suc.next.next = first_node  # 再接第1个节点
                node_be_suc.next.next.next = third_node
                # 迭代
                node_to_do = third_node
                node_be_suc = node_be_suc.next.next
            elif node_to_do is not None:
                node_be_suc.next = node_to_do
                break
            else:
                break

        return dummy.next


    def swapPairs(self, head):
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead


if __name__ == "__main__":
    # RUN
    s = Solution()

    # case1
    node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    node.print_to_the_end()
    result = s.swapPairs(node)
    result.print_to_the_end()

    # case2
    node = ListNode(1, None)
    result = s.swapPairs(node)
    result.print_to_the_end()

    # case3
    node = None
    result = s.swapPairs(node)
    print(result)
    # result.print_to_the_end
