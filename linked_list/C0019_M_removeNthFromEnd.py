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


    def removeNthFromEnd(self, head, n):
        """
        删除倒数第n个节点, 能否在一次循环完成?
        链表中结点的数目为 sz
        1 <= sz <= 30
        0 <= Node.val <= 100
        1 <= n <= sz
        :param head:ListNode
        :param n:int
        :return:ListNode
        """
        # 初始化头部
        ans_node = ListNode(val=0, next=head)
        deep = n-1              # 倒数深度
        delete_up_node = None   # 被删除节点的上一个节点
        delete_node = None      # 要删除的节点
        set_flag = False        # 是否第一次找到要删除的节点
        end_flag = False        # 结束标识符
        tmp = head              # 当前探查节点
        while not end_flag:
            # 下潜1
            tmp = tmp.next
            # 慢指针
            if deep != 0:
                deep -= 1
            else:
                if not set_flag:
                    delete_node = head
                    delete_up_node = ans_node
                    set_flag = True
                else:
                    delete_up_node = delete_up_node.next
                    delete_node = delete_node.next
            # 探底
            if tmp is None:
                end_flag = True
                # 删除节点
                delete_up_node.next = delete_node.next
        # 返回哑节点的下一个节点
        return ans_node.next

if __name__ == "__main__":
    s = Solution()
    node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    node.print_to_the_end()
    result = s.removeNthFromEnd(node, 5)
    result.print_to_the_end()