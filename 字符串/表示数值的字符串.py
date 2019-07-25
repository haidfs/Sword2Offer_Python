# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"
# 都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
# -*- coding:utf-8 -*-
import re
class Solution:
    # s字符串
    def isNumeric(self, s):
        if not s:
            return False
        s_processed = s.strip()
        if not s_processed:
            return False
        # 注意使用括号分割，不用括号则认为是左边或者右边部分满足就可以了
        if re.match(r"^(\+|\-?)\d+$", s_processed) or re.match(r"^(\+|\-?)\d*\.\d+$", s_processed) or re.match(
                r"^(\+|\-?)\d+(e|E)(\+|\-?)\d+$", s_processed) or re.match(r"^(\+|\-?)\d+\.\d+(e|E)(\+|\-?)\d+$",
                                                                           s_processed):
            return True
        else:
            return False