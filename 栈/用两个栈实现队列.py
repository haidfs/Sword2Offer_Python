# 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
class Solution:
    def __init__(self):
        self.stackIn = []
        self.stackOut = []

    def push(self, element):
        self.stackIn.append(element)
        return self

    def pop(self):
        if len(self.stackOut) == 0:
            if len(self.stackIn) == 0:
                return None
            else:
                while len(self.stackIn) > 0:
                    self.stackOut.append(self.stackIn.pop(-1))
                return self.stackOut.pop(-1)
        else:
            return self.stackOut.pop(-1)
