class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_self(self):
        tmp = self
        res = []
        while tmp is not None:
            res.append(tmp.val)
            tmp = tmp.next
        print(res)

def generateListNode(nums):
    res = ListNode()
    last = res
    for each in nums:
        tmp = ListNode(each, None)
        last.next = tmp
        last = tmp
    return res.next

class Solution:
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

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        "你可以使用一趟扫描完成反转吗？"
        res = ListNode()
        res.next = head
        # -----------------------------
        if left == right:
            return res.next
        # -----------------------------

        handle = res
        count = 0
        while True:
            # 当前为链表第i项
            this_node = handle.next
            count += 1
            if this_node == None:
                break
            if count == left:
                left_node = this_node
                head_node = handle
            elif count == right:
                right_node = this_node
                tail_node = this_node.next
                # 干活----------------------
                left_node, right_node = self.reverse(left_node, right_node)
                # 重新拼接
                head_node.next = left_node
                break
            # ITERATION
            handle = this_node
        return res.next


if __name__ == '__main__':
    s = Solution()
    node = generateListNode([1,2,3,4,5,6,7])
    result = s.reverseBetween(node, 2, 4)
    result.print_self()
