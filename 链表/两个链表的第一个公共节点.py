class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, list1, list2):
        if not list1 or not list2:
            return None
        stack1, stack2 = [], []
        while list1:
            stack1.insert(0, list1)
            list1 = list1.next
        while list2:
            stack2.insert(0, list2)
            list2 = list2.next
        len1, len2 = len(stack1), len(stack2)
        length = len1 if len1 <= len2 else len2
        flag = False
        for i in range(length):
            if stack1[i] != stack2[i]:
                if i == 0:  # 如果一开始就不相等，则表示二者不具备公共节点
                    return None
                flag = True
                break
        if not flag:
            return stack1[i]
        return stack1[i - 1]


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
    # n6.next = n7
    s = Solution()
    print(s.FindFirstCommonNode(n1, n1))
