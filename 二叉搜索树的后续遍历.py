# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, after_list):
        if not after_list:
            return False
        length = len(after_list)
        if length == 0:
            return False
        return self.judge(after_list, 0, length - 1)
    def judge(self, sequence, first, last):
        if first >= last:
            return True
        root = sequence[last]
        for i in range(last - 1, first - 1, -1):
            if sequence[i] < root:
                index = i
                break
        if i == first:
            return True
        for i in range(index, first - 1, -1):
            if sequence[i] > root:
                return False
        return self.judge(sequence, first, index) and self.judge(sequence, index + 1, last - 1)