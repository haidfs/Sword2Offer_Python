class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def PrintTreeFromUpToBottle(self, root):
        res =[]
        if not root:
            return None
        current_layer =[root]
        while current_layer:
            next_layer = []
            for i in current_layer:
                res.append(i.val)
                if i.left:
                    next_layer.append(i.left)
                if i.right:
                    next_layer.append(i.right)
            current_layer=next_layer
        return res
if __name__ == '__main__':
    n1 = TreeNode(8)
    n2 = TreeNode(6)
    n3 = TreeNode(10)
    n4 = TreeNode(5)
    n5 = TreeNode(7)
    n6 = TreeNode(9)
    n7 = TreeNode(11)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    s = Solution()
    print(s.PrintTreeFromUpToBottle(n1))
