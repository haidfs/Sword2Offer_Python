# -*- coding:utf-8 -*-
# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
class Solution:
    def Find1(self, element, array):
        row_num = len(array)
        col_num = len(array[0])
        if col_num == 0:
            return False
        for i in range(row_num):
            for j in range(col_num):
                if element == array[i][j]:
                    return True
        return False

    def Find2(self, element, array):
        row_num = len(array)
        col_num = len(array[0])
        if col_num == 0:
            return False
        for i in range(row_num - 1, -1, -1):
            if element == array[i][0]:
                return True
            elif element < array[i][0]:
                continue
            else:
                for j in range(col_num):
                    if element == array[i][j]:
                        return True
        return False


if __name__ == '__main__':
    s = Solution()
    a = [[1, 2, 3, 4], [5, 9, 13, 17], [6, 10, 14, 18], [7, 11, 15, 19]]
    print(s.Find1(a, 18))
    print(s.Find2(a, 17))