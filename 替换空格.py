# -*- coding:utf-8 -*-
# 请实现一个函数，将一个字符串中的每个空格替换成“%20”。
# 例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
class Solution:
    # s 源字符串
    def replaceSpace(self, str1):
        new_str = ''
        for i in range(len(str1)):
            if str1[i] == ' ':
                new_str = new_str + ('%20')
            else:
                new_str = new_str + (str1[i])
        return new_str


if __name__ == '__main__':
    ch = "we are happy"
    s = Solution()
    print(s.replaceSpace(ch))
