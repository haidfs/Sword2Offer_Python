class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 解题思路，利用之前的层序打印二叉树的方法，从左至右层序打印的结果等于从右至左打印的结果即可
# 牛客好几道题目都是我的ide可以通过，但是在线提交不过，很迷。也许是因为我用的是Python3，牛客的调试的是Python2吧。
# 不通过
# 您的代码已保存
# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为50.00%
#
# 用例:
# {5,3,3,4,#,#,4,2,#,#,2,#,#,#,1}
# 对应输出应该为:
# false
# 你的输出为:
# true

class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        left = self.treeLayerList(pRoot, "left")
        right = self.treeLayerList(pRoot, "right")
        if left == right:
            return True
        return False

    def treeLayerList(self, root, order):
        res = []
        temp = []
        if not root:
            return res
        temp.append(root)
        while temp:
            current_root = temp.pop(0)
            res.append(current_root.val)
            if order == "left":
                if current_root.left:
                    temp.append(current_root.left)
                if current_root.right:
                    temp.append(current_root.right)
            else:
                if current_root.right:
                    temp.append(current_root.right)
                if current_root.left:
                    temp.append(current_root.left)

        return res


# 于是换一种方法试试，仍然是递归，每一层直接比吧，虽然是递归，也不必利用之前列表作为辅助的结果
class Solution2:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        return self.isSame(pRoot.left, pRoot.right)

    def isSame(self, left, right):
        if not left and not right:
            return True
        if left and right and left.val == right.val:
            return self.isSame(left.left, right.right) and self.isSame(left.right, right.left)
        return False


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n8 = TreeNode(8)
    n9 = TreeNode(9)
    n10 = TreeNode(10)
    n11 = TreeNode(11)
    n12 = TreeNode(12)
    n13 = TreeNode(13)
    n14 = TreeNode(14)
    n15 = TreeNode(15)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8
    n4.right = n9
    n5.left = n10
    n5.right = n11
    n6.left = n12
    n6.right = n13
    n7.left = n14
    n7.right = n15

    s = Solution()
    print(s.isSymmetrical(n1))
