from C0000_ClassTree import *

class Solution:
    from typing import List
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        """输入两棵二叉搜索树, 返回全升序排列"""
        # 二叉搜索树的中序排列是升序的
        def midorder(node, res):
            if node is not None:
                midorder(node.left,res)
                res.append(node.val)
                midorder(node.right,res)

        nums1 = []
        nums2 = []
        answer = []
        p, q = 0, 0
        midorder(root1, nums1)
        midorder(root2, nums2)
        print(nums1, nums2)
        while True:
            print(p, len(nums1),q, len(nums2))
            if p>=len(nums1):
                if q< len(nums2):
                    answer.append(nums2[q])
                    q=q+1
                    continue
                else:
                    break
            if q>=len(nums2):
                if p< len(nums1):
                    answer.append(nums1[p])
                    p=p+1
                    continue
                else:
                    break
            if nums1[p]<=nums2[q]:
                answer.append(nums1[p])
                p+=1
            else:
                answer.append(nums2[q])
                q+=1
        return answer

if __name__ == '__main__':
    s = Solution()
    tree2 = generateTreeNode(None, [5,4,3,2,1,null,null])
    tree1 = generateTreeNode(None, [1])
    result = s.getAllElements(tree1, tree2)
    print(result)
