# 输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
# 这和二叉树的层序打印，是同一类型的题目
from math import fabs


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def TreeDepth(self, root):
        tree_depth = 0
        if not root:
            return tree_depth
        current_layer = [root]

        while current_layer:
            next_layer = []
            for i in current_layer:
                if i.left:
                    next_layer.append(i.left)
                if i.right:
                    next_layer.append(i.right)
            tree_depth += 1
            current_layer = next_layer
        return tree_depth


if __name__ == '__main__':
    n1 = TreeNode(8)
    n2 = TreeNode(6)
    n3 = TreeNode(10)
    n4 = TreeNode(5)
    n5 = TreeNode(7)
    n6 = TreeNode(9)
    n7 = TreeNode(11)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    s = Solution()
    print(s.TreeDepth(n1))
