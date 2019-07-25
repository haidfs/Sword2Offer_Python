# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, head):
        try:
            slow = head.next
            fast = head.next.next
            while fast != slow:
                slow = slow.next
                fast = fast.next.next
            h = head
            while h != fast:
                h = h.next
                fast = fast.next
            return h
        except:
            return None