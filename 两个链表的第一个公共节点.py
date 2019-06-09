class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, list1, list2):
        if not list1 or not list2:
            return None
        temp1 = list1
        temp2 = list2
        length1, length2 = 1, 1
        while temp1.next:
            length1 += 1
            temp1 = temp1.next
        while temp2.next:
            length2 += 1
            temp2 = temp2.next
        root1 = list1
        root2 = list2
        if length1 < length2:
            for i in range(length2 - length1):
                root2 = root2.next
        if length1 > length2:
            for i in range(length1 - length2):
                root1 = root1.next
        while root1 and root2:
            if root1.val == root2.val:
                return root1.val
            else:
                root1 = root1.next
                root2 = root2.next
        return None


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)
    n7 = ListNode(7)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n7
    n5.next = n6
    n6.next = n7
    s = Solution()
    print(s.FindFirstCommonNode(n1, n5))
