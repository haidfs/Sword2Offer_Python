# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


# 分为递归方法与非递归方法
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # 递归方法
        if not pHead:
            return
        new_node = RandomListNode(pHead.label)
        new_node.random = pHead.random
        new_node.next = self.Clone(pHead.next)
        return new_node

    def Clone2(self, pHead):
        # 非递归方法：第一步在原链表的基础上复制节点，将节点复制在原节点的后面。第二步复制随机节点。 第三步将新旧链表分离。
        # 个人认为，出题者的意图其实是希望我们使用这种方法的，因为第一步考查了链表的插入，第三步考查了链表的删除，题目设计的还是有些意思的。
        if not pHead:
            return None
        # 第一步复制原本链表的节点并插入在原节点的后面
        pCur = pHead
        while pCur:
            new_node = RandomListNode(pCur.label)
            new_node.next = pCur.next
            pCur.next = new_node
            pCur = new_node.next
        # 第二步复制随机节点
        pCur = pHead
        while pCur:
            if pCur.random:
                pCur.next.random = pCur.random.next
            pCur = pCur.next.next
        # 新旧链表的分离，涉及到链表节点的删除
        pCur = pHead
        new_head = pHead.next
        new_cur = new_head
        while pCur:
            pCur.next = pCur.next.next
            if new_cur.next:
                new_cur.next = new_cur.next.next
            new_cur = new_cur.next
            pCur = pCur.next
        return new_head
