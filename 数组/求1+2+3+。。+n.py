# 求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        return sum(list(range(1, 1 + n)))


# 思路二
# -*- coding:utf-8 -*-
class Solution2:
    def __init__(self):
        self.ans = 0

    def Sum_Solution(self, n):
        self.recur(n)
        return self.ans

    def recur(self, n):
        self.ans += n
        n -= 1
        return n > 0 and self.Sum_Solution(n)


if __name__ == '__main__':
    s = Solution2()
    print(s.Sum_Solution(100))

# 利用位运算来实现乘法？可以考虑，其中应该涉及到if和while
