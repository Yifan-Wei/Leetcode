from C0000_ClassTree import *
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        cur = root
        while cur:
            # 遍历当前层的时候，为了方便操作在下一层前面添加一个哑结点
            # （注意这里是访问当前层的节点，然后把下一层的节点串起来）
            dummy = TreeNode(0)
            # pre表示访下一层节点的前一个节点
            pre = dummy
            # 然后开始遍历当前层的链表
            while cur:
                if cur.left:
                    pre.next = cur.left
                    pre = pre.next
                if cur.right:
                    pre.next = cur.right
                    pre = pre.next
                # 访问本层的下一节点
                cur = cur.next
            # 把下一层串联成一个链表之后, 把头部赋值给cur，
            # 后续继续循环, 直到cur为空为止
            cur = dummy.next
        return root

if __name__ == '__main__':
    s = Solution()
    tree = generateTreeNode(None, [1,2,4,null,null,5,null,null,3,6,null,null,7,null,null])
    result = s.connect(tree)
    print(result)
