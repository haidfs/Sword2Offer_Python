# 输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from copy import deepcopy
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, target):
        current_path = []
        path_array = []
        self.find(root, target, current_path, path_array)
        return path_array
    def find(self, root, target, current_path, path_array):
        if not root:
            return path_array
        current_path.append(root.val)
        if sum(current_path) == target and not root.left and not root.right:
            path_array.append(deepcopy(current_path))
        # elif sum(current_path) < target:
        else:
            if root.left:
                self.find(root.left, target, current_path, path_array)
                current_path.pop(-1)
            if root.right:
                self.find(root.right, target, current_path, path_array)
                current_path.pop(-1)
        # elif sum(current_path) > target:
        #     current_path.pop(-1)