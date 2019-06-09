# 输入一棵二叉树，判断该二叉树是否是平衡二叉树。
# 首先什么是平衡二叉树，满足条件为null 或者任一节点的左子树深度和右子树深度差值的绝对值小于等于1
from math import fabs


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def IsBalanced_Solution(self, pRoot):
        # 确实是需要递归的，一般对于树来说都是根节点做判断，左右递归
        if not pRoot:
            return True
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        if fabs(left - right) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        left = self.TreeDepth(pRoot.left) + 1
        right = self.TreeDepth(pRoot.right) + 1
        return max(left, right)


if __name__ == '__main__':
    n1 = TreeNode(8)
    n2 = TreeNode(8)
    n3 = TreeNode(7)
    n4 = TreeNode(9)
    n5 = TreeNode(2)
    n6 = TreeNode(100)
    n7 = TreeNode(100)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    s = Solution()
    print(s.IsBalanced_Solution(n1))
