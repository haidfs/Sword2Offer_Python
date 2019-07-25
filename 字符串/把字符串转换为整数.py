# 将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
# 要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
# 输入描述:
# 输入一个字符串,包括数字字母符号,可以为空
# 输出描述:
# 如果是合法的数值表达则返回该数字，否则返回0
# 示例1
# 输入
# 复制
# +2147483647
#     1a33
# 输出
# 复制
# 2147483647
#     0
# -*- coding:utf-8 -*-
import re
class Solution:
    def StrToInt(self, s):
        if not s:
            return 0
        s_processed = s.strip()
        if not s_processed:
            return 0
        num = 0
        weishu = 1
        # 用一个正则表达式来进行匹配
        if re.match(r"^(\+|\-)?\d+$", s_processed):
            length = len(s_processed)
            if '+' in s_processed or '-' in s_processed:
                s_num = s_processed[1:]
                length -= 1
            else:
                s_num = s_processed
            for i in range(length - 1, -1, -1):
                num += int(s_num[i]) * weishu
                weishu = weishu * 10
            if s_processed[0] == '-':
                num = -num
            return num
        else:
            return 0