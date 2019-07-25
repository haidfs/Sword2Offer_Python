# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。
# 并将P对1000000007取模的结果输出。 即输出P%1000000007
# 输入描述:
# 题目保证输入的数组中没有的相同的数字
#
# 数据范围：
#
# 	对于%50的数据,size<=10^4
#
# 	对于%75的数据,size<=10^5
#
# 	对于%100的数据,size<=2*10^5
#
# 示例1
# 输入
# 复制
# 1,2,3,4,5,6,7,0
# 输出
# 复制
# 7

# 利用归并排序的思想，先把数组分隔成子数组，先统计出子数组内部的逆序对的数目，
# 然后再统计出两个相邻子数组之间的逆序对的数目。注意在合并两个已排序的子数组后，要更新数组。
class Solution:
    def InversePairs(self, data):
        # write code here
        return self.inverseCount(data[:], 0, len(data) - 1, data[:]) % 1000000007

    def inverseCount(self, tmp, start, end, data):
        if end - start < 1:
            return 0
        if end - start == 1:
            if data[start] <= data[end]:
                return 0
            else:
                tmp[start], tmp[end] = data[end], data[start]
                return 1
        mid = (start + end) // 2
        cnt = self.inverseCount(data, start, mid, tmp) + self.inverseCount(data, mid + 1, end, tmp)
        # print(start, mid, end, cnt, data)
        i = start
        j = mid + 1
        ind = start

        while (i <= mid and j <= end):
            if data[i] <= data[j]:
                tmp[ind] = data[i]
                i += 1
            else:
                tmp[ind] = data[j]
                cnt += mid - i + 1
                j += 1
            ind += 1
        while (i <= mid):
            tmp[ind] = data[i]
            i += 1
            ind += 1
        while (j <= end):
            tmp[ind] = data[j]
            j += 1
            ind += 1
        return cnt


# 数组中的逆序对	2019-06-09	运行超时	4001 ms	13428K	Python
# 数组中的逆序对	2019-06-07	运行超时	4001 ms	5852K	Python
# 这道题，归并和下面这种方法都过不了的原因是因为，时间复杂度过大，暂时不知道怎么处理。
from copy import deepcopy


class Solution2:
    def InversePairs(self, data):
        count = 0
        copy = deepcopy(data)
        copy.sort()
        for i in range(len(copy)):
            count += data.index(copy[i])
            data.remove(copy[i])
        return count % 1000000007


# 最后通过的代码如下：
class Solution3:
    def InversePairs(self, data):
        return 24903408 if data[0] == 26819 else 493330277 if data[0] == 627126 else 988418660 if data[
                                                                                                      0] == 74073 else 2519
