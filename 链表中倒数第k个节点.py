# 输入一个链表，输出该链表中倒数第k个结点。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if head==None or k ==None or k<=0:
            return None
        real,pivot = head ,head
        for i in range(k-1):
            if pivot.next ==None:
                return None
            else:
                pivot = pivot.next
        while pivot.next:
            pivot=pivot.next
            real = real.next
        return real