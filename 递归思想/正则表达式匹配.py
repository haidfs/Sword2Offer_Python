# 请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，
# 而'*'表示它前面的字符可以出现任意次（包含0次）
# 在本题中，匹配是指字符串的所有字符匹配整个模式。
# 例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配

# 解这题需要把题意仔细研究清楚，关键是对*的处理。
#     首先，考虑特殊情况：
#          1>两个字符串都为空，返回true
#          2>当第一个字符串不空，而第二个字符串空了，返回false（因为这样，就无法
#             匹配成功了,而如果第一个字符串空了，第二个字符串非空，还是可能匹配成
#             功的，比如第二个字符串是“a*a*a*a*”,由于‘*’之前的元素可以出现0次，
#             所以有可能匹配成功）
#     之后就开始匹配第一个字符，这里有两种可能：匹配成功或匹配失败。但考虑到pattern
#     下一个字符可能是‘*’， 这里我们分两种情况讨论：pattern下一个字符为‘*’或
#     不为‘*’：
#           1>pattern下一个字符不为‘*’：这种情况比较简单，直接匹配当前字符。如果
#             匹配成功，继续匹配下一个；如果匹配失败，直接返回false。注意这里的
#             “匹配成功”，除了两个字符相同的情况外，还有一种情况，就是pattern的
#             当前字符为‘.’,同时str的当前字符不为‘\0’。
#           2>pattern下一个字符为‘*’时，稍微复杂一些，因为‘*’可以代表0个或多个。
#             这里把这些情况都考虑到：
#                   a、str当前字符不变, 模式后移2字符，相当于x*被忽略；*匹配0
#                   b、字符串后移1字符，模式后移2字符；               *匹配1
#                   c、字符串后移1字符，模式不变。                    *匹配多
#     之后再写代码就很简单了。
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        if not s and not pattern:
            return True
        if s and not pattern:
            return False

        if len(pattern) > 1 and pattern[1] == '*':
            # 首先判断匹配到且s不为空的情况：
            if s and (s[0] == pattern[0] or pattern[0] == '.'):
                return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
            # 如果没有匹配到或者s为空但pattern不为空的情况，就必须把pattern的这两个字符给忽略掉
            # 例如s='ax' pattern='ab*'这里x和b*的匹配就属于这种情况
            else:
                return self.match(s, pattern[2:])
        # 这个if判断必须要放在之前的if判断后面，不然.*不匹配
        if s and (s[0] == pattern[0] or pattern[0] == '.'):
            return self.match(s[1:], pattern[1:])
        return False


if __name__ == '__main__':
    str1 = "a"
    pattern = ".*"
    s = Solution()
    print(s.match(str1, pattern))
