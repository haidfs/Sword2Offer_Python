# -*- coding:utf-8 -*-
# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
# 二叉搜索树的性质如下，中序遍历就可以得到排序好的数组
# 1、如果节点的左子树不空，则左子树上所有结点的值均小于等于它的根结点的值；
# 2、如果节点的右子树不空，则右子树上所有结点的值均大于等于它的根结点的值；
# 3、任意节点的左、右子树也分别为二叉查找树；
# 这里是https://blog.csdn.net/u010005281/article/details/79657259的代码

class Solution:
    def __init__(self):
        self.listHead = None
        self.listTail = None

    def Convert(self, pRootOfTree):
        # 不会的原因是对递归总是理解的不深刻
        # 中序遍历总是会递归到最左边的叶子节点的，这里的代码只需要对中序遍历进行稍微的改动就可以了
        if not pRootOfTree:
            return
        self.Convert(pRootOfTree.left)
        if not self.listHead:
            # 会递归到最左边的叶子节点的，首先把双向链表的头和尾进行初始化
            self.listHead = pRootOfTree
            self.listTail = pRootOfTree
        else:
            self.listTail.right = pRootOfTree
            pRootOfTree.left = self.listTail
            self.listTail = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.listHead

    # # 将二叉树转换为有序双向链表
    # def Convert(self, pRootOfTree):
    #     if pRootOfTree == None:
    #         return
    #     self.Convert(pRootOfTree.left)
    #     if self.listHead == None:
    #         self.listHead = pRootOfTree
    #         self.listTail = pRootOfTree
    #     else:
    #         self.listTail.right = pRootOfTree
    #         pRootOfTree.left = self.listTail
    #         self.listTail = pRootOfTree
    #     self.Convert(pRootOfTree.right)
    #     return self.listHead

    # 获得链表的正向序和反向序
    def printList(self, head):
        while head.right:
            print(head.val, end=" ")
            head = head.right
        print(head.val)
        while head:
            print(head.val, end=" ")
            head = head.left

    # 给定二叉树的前序遍历和中序遍历，获得该二叉树
    def getBSTwithPreTin(self, pre, tin):
        if len(pre) == 0 | len(tin) == 0:
            return None

        root = TreeNode(pre[0])
        for order, item in enumerate(tin):
            if root.val == item:
                root.left = self.getBSTwithPreTin(pre[1:order + 1], tin[:order])
                root.right = self.getBSTwithPreTin(pre[order + 1:], tin[order + 1:])
                return root


class TreeNode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x


if __name__ == '__main__':
    solution = Solution()
    preorder_seq = [4, 2, 1, 3, 6, 5, 7]
    middleorder_seq = [1, 2, 3, 4, 5, 6, 7]
    treeRoot1 = solution.getBSTwithPreTin(preorder_seq, middleorder_seq)
    head = solution.Convert(treeRoot1)
    solution.printList(head)

    #      4
    #    /   \
    #   2     6
    #  / \   / \
    # 1   3 5   7
