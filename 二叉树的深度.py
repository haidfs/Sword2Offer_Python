# 输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
# 这和二叉树的层序打印，是同一类型的题目
from math import fabs


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 同样分为递归和非递归方法
class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        curLevelNodeList = [pRoot]
        length = 0
        while curLevelNodeList:
            temp = []
            for i in curLevelNodeList:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            length += 1
            curLevelNodeList = temp
        return length

    def TreeDepth2(self, pRoot):
        if not pRoot:
            return 0
        left = self.TreeDepth2(pRoot.left) + 1
        right = self.TreeDepth2(pRoot.right) + 1
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
    n4.left = n6
    n6.right = n7
    s = Solution()
    print(s.TreeDepth2(n1))
