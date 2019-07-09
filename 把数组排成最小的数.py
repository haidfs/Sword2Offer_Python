# 题目描述
# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，
# 则打印出这三个数字能排成的最小数字为321323。
# 其实感觉就是变向的冒泡排序，只不过修改了排序的规则，比较取巧的是利用str来进行判断，避免了使用for循环来算出数值大小再进行比较
class Solution:
    def PrintMinNumber(self, numbers):
        string = [str(num) for num in numbers]
        count = len(string) - 1
        while count > 0:
            for i in range(len(string) - 1):
                if self.theMax(string[i], string[i + 1]) == string[i]:
                    string[i], string[i + 1] = string[i + 1], string[i]
            count -= 1
        string = ''.join(string)
        return string

    def theMax(self, str1, str2):
        return str1 if str1 + str2 > str2 + str1 else str2


if __name__ == '__main__':
    arr = [3, 32, 321]
    s = Solution()
    print(s.PrintMinNumber(arr))
