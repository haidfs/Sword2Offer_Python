# -*- coding:utf-8 -*-
from collections import defaultdict


class Solution:
    def FirstNotRepeatingChar(self, str1):
        if not str1:
            return -1
        char_count = defaultdict(lambda : 0)
        for i in str1:
            char_count[i] += 1
        for i in range(len(str1)):
            if char_count[str1[i]] == 1:
                return i
        return -1


    c = "googllee"
    s = Solution()
    print(s.FirstNotRepeatingChar(c))
