# 小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,
# 他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就
# 得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!

# -*- coding:utf-8 -*-
from math import sqrt
class Solution:
    def FindContinuousSequence(self, target):
        res = []
        for num in range(1, target // 2 + 1):
            b = 2 * num - 1
            c = -2 * target
            for length in range(2, int((-b + sqrt(b ** 2 - 4 * c)) // 2) + 1):
                sum1 = (2 * num + length - 1) * length / 2
                if int(sum1) == target:
                    res.append((num, length))
        res_process = []
        for i in res:
            res_part = []
            res_part = list(range(i[0], i[0] + i[1]))
            # for j in range(i[1]):
            #     res_part.append(i[0] + j)
            res_process.append(res_part)

        return res_process