# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x


class Solution:
    # 开始是想写在一个函数里面的，但是很明显你的递归出口没法直接在这个函数里面设置
    def VerifySquenceOfBST(self, after_list):
        if not after_list or len(after_list) == 0:
            return False
        return self.judge(after_list, 0, len(after_list))

    def judge(self, after_list, start, end):
        if start >= end:
            return True
        lt_flag = False
        for i in range(end - 1, start - 1, -1):
            if after_list[i] < after_list[end - 1]:
                index = i
                lt_flag = True
                break
        if i == start and lt_flag:
            return True
        # 这个语句是为了对array1的类似情况进行判断
        if i == start and not lt_flag:
            return False
        for i in range(index, start - 1, -1):
            if after_list[i] >= after_list[end - 1]:
                return False
        return self.judge(after_list, start, index + 1) and self.judge(after_list, index + 1, end - 1)


if __name__ == '__main__':
    # array = [1, 2, 3, 4, 7, 6, 4]
    array1 = [4, 5, 2, 6, 7, 3, 1]
    array2 = [1, 3, 2, 5, 7, 6, 4]
    s = Solution()
    print(s.VerifySquenceOfBST(array1))
    print(s.VerifySquenceOfBST(array2))
