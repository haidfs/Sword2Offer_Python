# 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
# 注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
# 这题目和二叉搜索与双向链表比较接近，应当进行对比学习
# https://blog.csdn.net/wojiuguowei/article/details/84847817
# 1、有右子树的，那么下个结点就是右子树最左边的点；（eg：D，B，E，A，C，G）
# 下面的两种方式可以直接合成一种
# 2、没有右子树的，也可以分成两类，a)是父节点左孩子（eg：N，I，L） ，那么父节点就是下一个节点 ； b)是父节点的右孩子
# （eg：H，J，K，M）找他的父节点的父节点的父节点...直到当前结点是其父节点的左孩子位置。如果没有eg：M，那么他就是尾节点。
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return None
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
            # next是指向父节点的指针
        while pNode.next:
            pRoot = pNode.next
            if pRoot.left == pNode:
                return pRoot
            pNode = pNode.next
        # 如果向上一直找不到祖宗节点使得其处在左子树，意味着该节点本身就是尾节点
        return None
class Solution2:
    def GetNext(self, pNode):
        if not pNode:
            return None
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        # next是指向父节点的指针
        if pNode.next and pNode.next.left and pNode.next.left == pNode:
            return pNode.next
        pNode = pNode.next
        while pNode.next:
            pRoot = pNode.next
            if pRoot.left == pNode:
                return pRoot
            pNode = pNode.next
        # 如果向上一直找不到祖宗节点使得其处在左子树，意味着该节点本身就是尾节点
        return None
# 报错如下
# 用例:
# {5,4,#,3,#,2},5
#
# 对应输出应该为:
#
# "null"
#
# 你的输出为:
#
# 'NoneType' object has no attribute 'left'
#
