# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0

class Solution:
    def minNumberInRotateArray(self, array):
        if len(array) == 0:
            return 0
        #         这里很明显的看出来，数组里面有两段是直接排序好的，只要找到第一个a[i+1]<a[i]，那么就可以认为是最小值？这和jdk8里面的timsort与三轴快排类似，
        for i in range(len(array)):
            if array[i + 1] < array[i]:
                return array[i + 1]
        return array[0]