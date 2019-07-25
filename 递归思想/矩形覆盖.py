# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
class Solution:
    def rectCover(self, n):
        res, cur_num, pre_num = 0,2,1
        if n==1 or n==2:
            return n
        else:
            for i in range(2,n):
                res =cur_num + pre_num
                pre_num=cur_num
                cur_num=res
            return res