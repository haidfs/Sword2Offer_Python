# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
# 如果有多对数字的和等于S，输出两个数的乘积最小的

# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, S):
        left = 0
        right = len(array)
        num1, num2 = [], []
        for i in array:
            if i not in num1 and self.binarySearch(array, left, right, S - i) != -1:
                num1.append(i)
                num2.append(S - i)
        mul_list = []
        for i in range(len(num1)):
            mul_list.append(num1[i] * num2[i])
        if not mul_list:
            return []
        mul_list_index = sorted(range(len(mul_list)), key=lambda k: mul_list[k])
        min_index = mul_list_index[0]
        return num1[min_index], num2[min_index]

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
