# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）
class Solution:
    def jumpFloor(self, n):
        result, pre_num, cur_num = 0, 0, 1
        if n == 0 or n == 1:
            return n
        else:
            for i in range(1, n + 1):
                result = pre_num + cur_num
                pre_num = cur_num
                cur_num = result
            return result