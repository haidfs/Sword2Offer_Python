# 题目描述
# 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
# 但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
# 但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
# 这里感觉和回溯关系不大，count能算到多少，直接1+上下左右递归去计算就行。

class Solution:
    def movingCount(self, threshold, rows, cols):
        matrix = [[True for i in range(cols)] for j in range(rows)]
        result = self.findGrid(threshold, rows, cols, matrix, 0, 0)
        return result

    def judge(self, threshold, i, j):
        if sum(map(int, str(i) + str(j))) > threshold:
            return False
        return True

    def findGrid(self, threshold, rows, cols, matrix, i, j):
        count = 0
        if 0 <= i < rows and 0 <= j < cols and self.judge(threshold, i, j) and matrix[i][j]:
            matrix[i][j] = False
            count = 1 + self.findGrid(threshold, rows, cols, matrix, i - 1, j) + self.findGrid(threshold, rows, cols,
                                                                                               matrix, i,
                                                                                               j - 1) + self.findGrid(
                threshold, rows, cols, matrix, i + 1, j) + self.findGrid(threshold, rows, cols, matrix, i, j + 1)
        return count


if __name__ == '__main__':
    s = Solution()
    count = s.movingCount(9, 12, 12)
    print(count)
