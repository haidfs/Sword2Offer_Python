# 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self,head1, head2):
            if None == head1:
                return head2
            if None == head2:
                return head1
    # if head1.val < head2.val:
    #     new_head = head1
    #     temp = new_head
    # else:
    #     new_head = head2
    #     temp = new_head
            copy = None
            if head1.val < head2.val:
                copy = head1
                copy_copy = copy
                if head1.next:
                    head1 = head1.next
                else:
                    copy.next = head2
                    return copy_copy
            else:
                copy = head2
                copy_copy = copy
                if head2.next:
                    head2 = head2.next
                else:
                    copy.next = head1
                    return copy_copy
            while True:
                if head1.val < head2.val:
                    copy.next = head1
                    if head1.next:
                        head1 = head1.next
                    else:
                        copy = copy.next
                        copy.next = head2
                        return copy_copy
                else:
                    copy.next = head2
                    if head2.next:
                        head2 = head2.next
                    else:
                        copy = copy.next
                        copy.next = head1
                        return copy_copy
                copy = copy.next