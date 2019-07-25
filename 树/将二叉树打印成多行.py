# 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
# 和之字形打印二叉树是一样的，其实就是层序遍历求二叉树深度的一种变体，这是剑指offer里面题目的一贯风格，会让练习的人由浅入深的掌握。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        res = []
        if not pRoot:
            return []
        curLevelNodeList = [pRoot]
        while curLevelNodeList:
            temp = []
            for i in range(len(curLevelNodeList)):
                if curLevelNodeList[i].left:
                    temp.append(curLevelNodeList[i].left)
                if curLevelNodeList[i].right:
                    temp.append(curLevelNodeList[i].right)

            res_part = []
            for i in range(len(curLevelNodeList)):
                current_root = curLevelNodeList.pop(0)
                res_part.append(current_root.val)
            res.append(res_part)
            curLevelNodeList = temp
        return res

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
    print(str(s.Print(n1)))
