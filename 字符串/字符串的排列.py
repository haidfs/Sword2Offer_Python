# -*- coding:utf-8 -*-
# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c
# 所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
# 输入描述:
# 输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
# 字典序打印字符串所有排列
def Permutation(ss):
    # if not ss:
    if ss == '':
        print("end,")
    for i in range(len(ss)):
        print(ss[i])
        Permutation(ss[:i] + ss[i + 1:])


def Permutation2(ss):
    list = []
    if len(ss) <= 1:
        return ss
    for i in range(len(ss)):
        for j in map(lambda x: ss[i] + x, Permutation2(ss[:i] + ss[i + 1:])):
            # if j not in list:
            #     list.append(j)
            list.append(j)
    return list


class Solution:
#https://blog.csdn.net/shizhengxin123/article/details/79590349
    def __init__(self):
        self.result = []

    def Permutation(self, ss):
        # write code here
        s = []
        to = len(ss)
        for i in range(to):
            s.append(ss[i])
        self.PermutationHelper(s, 0, len(ss))
        self.result = list(set(self.result))
        self.result.sort()
        return self.result

    def PermutationHelper(self, ss, fro, to):
        if (to <= 0):
            return
        if (fro == to - 1):

            self.result.append(''.join(ss))
        else:
            for i in range(fro, to):
                self.swap(ss, i, fro)
                self.PermutationHelper(ss, fro + 1, to)
                self.swap(ss, fro, i)

    def swap(self, str, i, j):
        str[i], str[j] = str[j], str[i]


if __name__ == '__main__':
    # print(Permutation2('abc'))
    s = Solution()
    print(s.Permutation('abbc'))
    # end代表print的输出不再换行，而是加上结束字符，即end所带的参数
    # print('1', end='')
    # print("2")
    # print('3')

