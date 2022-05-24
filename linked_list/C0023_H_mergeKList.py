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
    def case1_mergeKLists(self, lists):
        """
        :param lists:  List[Optional[ListNode]]
        :return:Optional[ListNode]
        """
        dummy = ListNode()  # 哑节点
        tmp = dummy
        while len(lists):
            ii = len(lists)
            min_num = 2 ** 31 - 1
            p = None
            p2 = None
            for each in lists[::-1]:
                ii -= 1
                if each is not None and lists[ii].val < min_num:
                    min_num = lists[ii].val
                    p = lists[ii]
                    p2 = ii
            if p2 is not None:
                tmp.next = p
                lists[p2] = lists[p2].next
                tmp = tmp.next
            else:
                break
        return dummy.next

    def mergeKLists(self, lists):

        def mergeTwoLists(list1, list2):
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

        def merge_iter(input_list):
            if len(input_list) >= 2:
                tmp = mergeTwoLists(input_list[0], input_list[1])
                tmp_list = input_list[2:]
                tmp_list.append(tmp)
                return merge_iter(tmp_list)
            elif len(input_list):
                return input_list[0]
            else:
                return None
        return merge_iter(lists)


if __name__ == "__main__":
    node_list = []
    #node1 = ListNode(1, ListNode(4, ListNode(5)))
    #node2 = ListNode(1, ListNode(3, ListNode(4)))
    # node3 = ListNode(2, ListNode(6))
    #node_list.append(node1)
    #node_list.append(node2)
    #node_list.append(node3)
    # RUN
    s = Solution()
    result = s.mergeKLists(node_list)
    # result.print_to_the_end()
