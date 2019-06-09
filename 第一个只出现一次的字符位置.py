# 在一个字符串(0<=字符串长度<=10000，全部由字母组成)
# 中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.

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