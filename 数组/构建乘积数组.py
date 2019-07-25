# 给定一个数组A[0,1,...,n-1],请构建
# 一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
# -*- coding:utf-8 -*-
import copy
import functools

class Solution:
    def multiply(self, A):
        # write code here
        B = []
        for i in range(len(A)):
            a = copy.copy(A)
            a[i] = 1
            mul = functools.reduce(lambda x, y: x * y, a)
            B.append(mul)
        return B