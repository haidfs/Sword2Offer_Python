# -*- coding:utf-8 -*-
# 题目描述
# 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, head):
        if head == None or head.next == None:
            return []
        res = []
        while head:
            res.append(head.val)
            head = head.next
        res_recersed = []
        for i in range(len(res) - 1, -1, -1):
            res_recersed.append(res[i])
        return res_recersed