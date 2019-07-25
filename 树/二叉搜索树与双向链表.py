# -*- coding:utf-8 -*-
# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
# 考查知识点：中序遍历、双向链表的尾插法
# 二叉搜索树的性质如下，中序遍历就可以得到排序好的数组
# 1、如果节点的左子树不空，则左子树上所有结点的值均小于等于它的根结点的值；
# 2、如果节点的右子树不空，则右子树上所有结点的值均大于等于它的根结点的值；
# 3、任意节点的左、右子树也分别为二叉查找树；
# 这里是https://blog.csdn.net/u010005281/article/details/79657259的代码
class TreeNode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x


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
        if not self.listTail and not self.listHead:
            self.listHead = pRootOfTree
            self.listTail = pRootOfTree
        else:
            self.listTail.right = pRootOfTree
            pRootOfTree.left = self.listTail
            self.listTail = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.listHead




