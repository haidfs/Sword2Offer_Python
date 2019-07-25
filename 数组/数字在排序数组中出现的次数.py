# 统计一个数字在排序数组中出现的次数。
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, order_list, k):
        index = self.binarySearch(order_list, 0, len(order_list), k)
        if index == -1:
            return 0
        count = 0
        for i in range(index-1, -1, -1):
            if order_list[i] == k:
                index -= 1
        for i in range(index, len(order_list), 1):
            if order_list[i] == k:
                count += 1
        return count

    def binarySearch(self, order_list, left, right, target):
        if left >= right:
            return -1
        mid = (left + right) // 2
        if order_list[mid] == target:
            return mid
        elif order_list[mid] < target:
            return self.binarySearch(order_list, mid + 1, len(order_list), target)
        else:
            return self.binarySearch(order_list[:mid], 0, mid, target)