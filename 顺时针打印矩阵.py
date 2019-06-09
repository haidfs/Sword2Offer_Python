# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，
# 如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
# 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
# -*- coding:utf-8 -*-
#import numpy as np
class Solution:
    def __init__(self):
        self.res = []
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
      #  matrix = np.array(matrix)
        row_num = len(matrix)
        if row_num == 0:
            return self.res
        col_num = len(matrix[0])

        i = 0
        for j in range(col_num):
            self.res.append(matrix[i][j])
        if row_num == 1:
            return self.res
        for i in range(1, row_num):
            self.res.append(matrix[i][j])
        if col_num == 1:
            return self.res
        for j in range(col_num - 2, -1, -1):
            self.res.append(matrix[i][j])
        for i in range(row_num - 2, 0, -1):
            self.res.append(matrix[i][j])
        if len(self.res) == col_num * row_num:
            return self.res
        else:
            #return self.printMatrix(matrix[1:row_num - 1, 1:col_num - 1])
            return self.printMatrix([i[1:col_num-1] for i in matrix[1:row_num-1]])