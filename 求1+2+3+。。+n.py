# 求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.ans = 0
    def Sum_Solution(self, n):
        self.recur(n)
        return self.ans

    def recur(self, n):
        self.ans += n
        n -= 1
        return n > 0 and self.Sum_Solution(n)