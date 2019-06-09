# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
# 假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，
# 序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
# （注意：这两个序列的长度是相等的）
# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, push_list, pop_list):
        if push_list == None or pop_list == None:
            return False
        if len(push_list) != len(pop_list):
            return False
        stack = []
        index = 0
        while push_list:
            stack.append(push_list.pop(0))
            while stack:
                if stack[-1] == pop_list[index]:
                    stack.pop(-1)
                    index += 1
                else:
                    break
        return not stack
        # write code here