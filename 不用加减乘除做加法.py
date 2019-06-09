# -*- coding:utf-8 -*-
class Solution:
    def Add(self, carry, sum):
        if carry == 0:
        # return sum if sum <= 0x7FFFFFFF else ~(sum ^ 0xFFFFFFFF)
            return sum if sum <= 0x7FFFFFFF else -(~(sum - 1) & 0xFFFFFFFF)
        return self.Add((carry & sum) << 1, (carry ^ sum) & 0xFFFFFFFF)