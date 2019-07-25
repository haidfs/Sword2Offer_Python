class Solution:
    def GetUglyNumber_Solution(self, index):
        if index < 1:
            return 0
        t2, t3, t5 = 0, 0, 0
        res = [1]
        while len(res) < index:
            val = min(2 * res[t2], 3 * res[t3], 5 * res[t5])
            res.append(val)
            if res[-1] == res[t2] * 2:
                t2 += 1
            elif res[-1] == res[t3] * 3:
                t3 += 1
            else:
                t5 += 1
        return res[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.GetUglyNumber_Solution(4))
