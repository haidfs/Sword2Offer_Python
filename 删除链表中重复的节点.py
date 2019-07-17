# 在一个排序的链表中，存在重复的结点，请删除
# 该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, head):
        if not head or not head.next:
            return head
        current = head.next
        if head.val == current.val:
            while current and current.val==head.val:
                current = current.next
            return self.deleteDuplication(current)
        else:
            head.next = self.deleteDuplication(current)
            return head
