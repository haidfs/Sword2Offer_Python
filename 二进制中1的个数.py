# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
class Solution:
    def NumberOf1(self, n):
        count =0
        while n & 0xffffffff != 0:
            count += 1
            n =n& (n-1)
        return count