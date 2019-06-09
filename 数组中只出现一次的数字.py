# -*- coding:utf-8 -*-
# 一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
from collections import defaultdict
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        num_count = defaultdict(lambda: 0)
        for i in array:
            num_count[i] += 1
        num_count = sorted(num_count.items(), key=lambda x: x[1])
        return [num_count[0][0], num_count[1][0]]