# -*- coding:utf-8 -*-
# 把只包含质因子2、3和5的数称作丑数（Ugly Number）。
# 例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index < 1:
            return 0
        res = [1]
        t2, t3, t5 = 0, 0, 0
        while len(res) < index:
            minNum = (min(res[t2] * 2, res[t3] * 3, res[t5] * 5))
            if minNum > res[-1]: res.append(minNum)
            if res[-1] == res[t2] * 2:
                t2 += 1
            elif res[-1] == res[t3] * 3:
                t3 += 1
            else:
                t5 += 1
        return res[-1]