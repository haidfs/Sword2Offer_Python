# 请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第
# 一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
from collections import defaultdict


class Solution:
    def __init__(self):
        self.s = ''
        self.char_count = defaultdict(lambda: 0)

    # 返回对应char
    def FirstAppearingOnce(self):
        for i in self.s:
            if self.char_count[i] ==1:
                return i
        return '#'


    def Insert(self, char):
        self.s += char
        self.char_count[char]+=1

