# 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, node):
        self.stack.append(node)
        if len(self.min_stack)==0 or node < self.min():
            self.min_stack.append(node)
        # write code here
    def pop(self):
        if self.stack:
            pop_num = self.stack.pop(-1)
            if pop_num == self.min():
                self.min_stack.pop(-1)
            return pop_num
        else:
            return None
        # write code here
    def top(self):
        return self.min()
        # write code here
    def min(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return None
        # write code here