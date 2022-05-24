# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_self(self):
        list = []
        tmp = self
        while tmp is not None:
            list.append(tmp.val)
            tmp = tmp.next
        print(list)

def generateListNode(nums):
    res = ListNode()
    last = res
    for each in nums:
        tmp = ListNode(each, None)
        last.next = tmp
        last = tmp
    return res.next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    from typing import Optional
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if head is not None:
            handle = head
            cnt = 1
            while handle.next is not None:
                handle = handle.next
                cnt += 1
        else:
            cnt = 0
        # print("linked list length = ", cnt)
        def linked_list_to_bst(head, list_length):
            # print("now discuss length =", list_length)
            if head is None: return None
            if list_length == 0: return None
            if list_length == 1: return TreeNode(head.val, None, None)
            mid_loc = (list_length+1) // 2
            left_length = mid_loc - 1
            right_length = list_length - mid_loc
            mid_node = head
            ii = mid_loc-1
            while ii > 0:
                mid_node = mid_node.next
                ii -= 1
            mid_val = mid_node.val
            # print("tot length = {0}, left_length = {1}, right length = {2}, mid_val = {3}".format(list_length, left_length,
            #                                                                                       right_length, mid_val))
            return TreeNode(mid_val, linked_list_to_bst(head, left_length), linked_list_to_bst(mid_node.next, right_length))

        if cnt:
            return linked_list_to_bst(head, cnt)
        else:
            return None

if __name__ == '__main__':
    s = Solution()
    node = generateListNode([-10, -3, 0, 5, 9])
    node.print_self()
    result = s.sortedListToBST(node)
    print(result)
