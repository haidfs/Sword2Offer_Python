# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
# 打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        string = [str(num) for num in numbers]
        res = []
        flag = True
        count = len(string) - 1
        while flag and count > 0:
            flag = False
            for i in range(len(string) - 1):
                if self.theMax(string[i], string[i + 1]) == string[i]:
                    string[i], string[i + 1] = string[i + 1], string[i]
                    flag = True
            count -= 1
        string = ''.join(string)
        return string
    def theMax(self, str1, str2):
        return str1 if str1 + str2 > str2 + str1 else str2