# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
# n<=39
class Solution:
    def Fibonacci(self, n):
        result, pre_num, cur_num = 0, 0, 1
        if n == 0 or n == 1:
            return n
        else:
            for i in range(1, n):
                result = pre_num + cur_num
                pre_num = cur_num
                cur_num = result
            return result
