# 给定两个非空链表，链表中每一位存储一个数字，逆序代表一个数字，形如：5->4->3代表345
# 链表最后一位不会是零或者负数，求两个数字的加和
# 如果要两数相加, 很显然考虑对齐和进位, 由于倒叙存放, 所以实际上已经对齐了
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_self(self):
        print(self.val)
        if self.next is not None:
            self.next.print_self()


class Solution:
    def addTwoNumbers(self, l1, l2):
        lout = ListNode()
        # 循环部分
        end_flag = False
        # 初始化部分, 主要是为了第一次运算
        carry = 0
        l1_do = l1
        l2_do = l2
        lout_do = lout
        while not end_flag:
            # 处理
            if l1_do is None:
                add1 = 0
            else:
                add1 = l1_do.val
                l1_do = l1_do.next
            if l2_do is None:
                add2 = 0
            else:
                add2 = l2_do.val
                l2_do = l2_do.next
            # 加法计算
            add = add1 + add2 + carry  # 预加和
            lout_do.val = add % 10  # 余数
            carry = add // 10  # 整除
            # 当且仅当两个链表都没有取值, 且没有进位的时候, 循环跳出
            if (l1_do is None) and (l2_do is None) and (carry==0):
                end_flag = True
            else:
                tmp = ListNode()
                lout_do.next = tmp
                lout_do = tmp
        return lout

if __name__ == "__main__":
    # num1 = 8 -> 9 = 98
    # num2 = 7 -> 9 = 97
    num1 = ListNode(val=8, next=ListNode(val=9))
    num2 = ListNode(val=7, next=ListNode(val=9))
    a = Solution()
    result = a.addTwoNumbers(num1, num2)
    result.print_self()
