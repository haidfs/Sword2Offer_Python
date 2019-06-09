# 输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
class Solution:
    def GetLeastNumbers_Solution(self, lyst, k):
        left = 0
        right = len(lyst) - 1
        if k>right+1:
            return []
        if not lyst:
            return []
        if right == -1:
            return []
        return self.quickSort(lyst, left, right)[:k]

    def quickSort(self,lyst, left, right):
        if left >= right:
            return lyst
        i = left
        j = right
        temp = lyst[left]
        while i < j:
            while j >= temp and i < j: j -= 1
            while i <= temp and i < j: i += 1
            if i < j:
                lyst[i], lyst[j] = lyst[j], lyst[i]
        lyst[i], lyst[left] = lyst[left], lyst[i]
        self.quickSort(lyst, 0, i - 1)
        self.quickSort(lyst, i + 1, right)
        return lyst
