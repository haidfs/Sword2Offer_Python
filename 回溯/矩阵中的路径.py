# 题目描述
# 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，
# 每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。
# 例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
# 因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。

# 思路：这种问题一看就有八皇后问题的感觉，考查的知识点是回溯法。
# 递归就是嵌入式的多级中断
# 这里如果某一个点没有找到对应的序列的话，那么pathLength会回退到0，相应的visited也会回退到全部为False的状态

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if not matrix or len(matrix) != rows * cols or not path:
            return False
        visited = [False] * len(matrix)
        # pathLength = [0]
        pathLength = 0
        for i in range(rows):
            for j in range(cols):
                if self.hasPathHelper(matrix, rows, cols, j, i, visited, pathLength, path):
                    return True
        return False

    def hasPathHelper(self, matrix, rows, cols, x, y, visited, pathLength, path):
        '''
                :param matrix:字符矩阵
                :param rows:矩阵的行数
                :param cols:矩阵的列数
                :param path:需要寻找的路径
                :param x:当前位置的横坐标(对应列数)
                :param y:当前位置的纵坐标(对应行数)
                :param visited:访问标志数组
                :param pathlength:已经找到的路径长度
                :return:是否存在路径
                '''
        # if pathLength[0] == len(path):
        if pathLength == len(path):
            return True
        hasPath = False
        if 0 <= x < cols and 0 <= y < rows and not visited[y * cols + x] and matrix[y * cols + x] == path[
            pathLength]:
            visited[y * cols + x] = True
            pathLength += 1
            hasPath = self.hasPathHelper(matrix, rows, cols, x - 1, y, visited, pathLength, path) or self.hasPathHelper(
                matrix, rows, cols, x, y - 1, visited, pathLength, path) or self.hasPathHelper(matrix, rows, cols,
                                                                                               x + 1, y, visited,
                                                                                               pathLength,
                                                                                               path) or self.hasPathHelper(
                matrix, rows, cols, x, y + 1, visited, pathLength, path)
            if not hasPath:
                pathLength -= 1
                visited[y * cols + x] = False
        return hasPath


if __name__ == '__main__':
    matrix = 'abcesfcsadee'
    rows = 3
    cols = 4
    # path = 'bcced'
    path = 'abcb'
    s = Solution()
    print(s.hasPath(matrix, rows, cols, path))
