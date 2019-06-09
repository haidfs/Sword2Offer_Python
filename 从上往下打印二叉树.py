# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        res = []
        temp = []
        if not root:
            return res
        temp.append(root)
        while temp:
            current_root = temp.pop(0)
            res.append(current_root.val)
            if current_root.left:
                temp.append(current_root.left)
            if current_root.right:
                temp.append(current_root.right)
        return res


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
    print(s.PrintFromTopToBottom(n1))
