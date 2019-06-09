# 请实现两个函数，分别用来序列化和反序列化二叉树
# 序列化是一种对象流的机制，序列化后可以使得对象便于在网络中进行传输
# 这里的序列化应该是指将二叉树转化为字符串的一种方式，前中后应该都可以，但是需要反序列化，所以需要加上分隔符。同时需要注意的是
# 如果遇到了空节点，也需要以特殊字符来标记。我们知道仅仅凭借任一中纯数字的二叉树的遍历，是无法反推二叉树的。
# 采用中序遍历来实现。如何通过层序遍历来进行序列化和反序列化？
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Serialize(self, pRoot):
        if not pRoot:
            return '#'
        return str(pRoot.val) + ',' + self.Serialize(pRoot.left) + ',' + self.Serialize(pRoot.right)

    def Deserialize(self, s):
        lyst = s.split(',')
        return self.deserializeTree(lyst)

    def deserializeTree(self, lyst):
        if not lyst:
            return None
        val = lyst.pop(0)
        root = None
        if val != "#":
            root = TreeNode(int(val))
            root.left = self.deserializeTree(lyst)
            root.right = self.deserializeTree(lyst)
        return root


# 确实是可以通过前序的方式来进行序列化的，但是通过其他的方式来进行序列化和反序列化？？
class Solution2:
    pass


if __name__ == '__main__':
    if __name__ == '__main__':
        for i in range(1, 16):
            exec("n%s = TreeNode(%s)" % (i, i))
        parent = [1, 2, 3, 4, 5, 6, 7]
        left = [i for i in range(2, 16, 2)]
        right = [i for i in range(3, 17, 2)]
        for i, j, k in zip(parent, left, right):
            exec("n%s.left = n%s" % (i, j))
            exec("n%s.right = n%s" % (i, k))
        s = Solution()
        c = s.Serialize(n1)
        de = s.Deserialize(c)
        print(c)
        print(de)
