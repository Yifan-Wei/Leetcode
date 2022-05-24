# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def numTrees(self, n: int) -> int:
        # 动态规划
        G = [0] * (n+1)  # G(n) 代表长度为N的序列能够构成不同二叉搜索树的个数
        # F = [[0]*n for _ in range(n)] # F(i, n)代表以i为根节点的长度为n的不同二叉树的个数
        # 对每个n均有 G = sigma(i) F(i,n)
        # 又有: F(i,n) = G(i-1)*G(n-i)  根节点在中央, 左边i-1个数, 右边n-i个数
        # 因此G(n) = sigma(i) G(i-1)*G(n-i)
        G[0] = 1  # 空树也是一棵
        G[1] = 1
        for ii in range(2, n+1):
            for jj in range(1, ii+1):
                G[ii] = G[ii] + G[jj-1]*G[ii-jj]
        return G[n]

if __name__ == '__main__':
    s = Solution()
    result = s.numTrees(3)
    print(result)
