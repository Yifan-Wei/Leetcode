# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    from typing import List
    def generateTrees(self, n: int) -> List[TreeNode]:
        dp = [[] for _ in range(n+1)]
        dp[0] = [[None]]
        # dp[1] = [[1, None]]

        def generateTreeNode(root, val):
            # val值用完了
            if len(val) == 0:
                return root
            # 当前节点是否为空
            if val[0] is not None:
                root = TreeNode(val[0])
                val.pop(0)
                # root.left/root.right默认就是None, 形成递归
                root.left = generateTreeNode(root.left, val)
                root.right = generateTreeNode(root.right, val)
                return root
            else:
                root = None
                val.pop(0)
                return root

        def transfer(add_num, num):
            res = num.copy()
            # print("<><><><><>")
            # print(add_num, res)
            if res is not None and add_num>0:
                for ii in range(len(res)):
                    if res[ii] is not None:
                        res[ii] += add_num
            # print(res)
            return res


        for ii in range(1, n+1):                    # ii是长度为ii
            for jj in range(0, ii+1):               # jj是底层循环
                for each_one in dp[jj-1]:
                    for each_other in dp[ii-jj]:
                        #print("....................")
                        #print(ii,jj,each_one,each_other)
                        ans = []
                        ans += [jj]
                        ans += transfer(0, each_one)
                        ans += transfer(jj, each_other)
                        #print("ANS:", ans)
                        dp[ii].append(ans)
                        #print("....................")
        # print(dp[n])
        res = []
        for each in dp[n]:
            res.append(generateTreeNode(None, each))
        return res

    def generateTrees2(self, n: int) -> List[TreeNode]:
        def generateTrees(start, end):
            if start > end:
                return [None, ]
            allTrees = []
            for i in range(start, end + 1):  # 枚举可行根节点
                # 获得所有可行的左子树集合
                leftTrees = generateTrees(start, i - 1)
                # 获得所有可行的右子树集合
                rightTrees = generateTrees(i + 1, end)
                # 从左子树集合中选出一棵左子树，从右子树集合中选出一棵右子树，拼接到根节点上
                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)
            return allTrees

        return generateTrees(1, n) if n else []

if __name__ == '__main__':
    s = Solution()
    result = s.generateTrees(3)
    print(result)
