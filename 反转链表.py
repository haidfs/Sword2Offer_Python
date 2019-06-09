# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, head):
        if head == None or head.next == None:
            return head
        left, medium, right = None, None, head
        while right.next:
            left = medium
            medium = right
            right = right.next
            medium.next = left
        right.next = medium
        return right