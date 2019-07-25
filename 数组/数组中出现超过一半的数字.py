# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入
# 一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
# -*- coding:utf-8 -*-
from collections import defaultdict
class Solution:
    def MoreThanHalfNum_Solution(self, lyst):
        length = len(lyst)
        half = length / 2
        dyct = defaultdict(lambda: 0)
        res = []
        for i in lyst:
            dyct[i] += 1
            if dyct[i] > half:
                return i
        return 0