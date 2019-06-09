# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 这里的想法是有问题的，所谓树的子结构不一定两棵树中序遍历后就是子串的关系。
class Solution2:
    def HasSubtree(self, b, a):
        mid_b = self.midTraverse(b)
        if mid_b == []:
            return False
        mid_a = self.midTraverse(a)
        return set(mid_b).issubset(set(mid_a))

    def midTraverse(self, root):
        if not root:
            return []
        res = []
        res += self.midTraverse(root.left)
        res.append(root.val)
        res += self.midTraverse(root.right)

        return res


class Solution3:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.is_subtree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right,
                                                                                                          pRoot2)

    def is_subtree(self, A, B):
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return self.is_subtree(A.left, B.left) and self.is_subtree(A.right, B.right)


# 和树相关的问题，天然的就应该想到递归的算法。
# 1、首先设置标志位res = false，因为一旦匹配成功result就设为true，剩下的代码不会执行，如果匹配不成功，默认返回false。
# 为了代码简洁这个标志位可以取消，直接返回true或者false即可。
# 2、递归思想，如果根节点相同则递归调用is_subtree(self, A, B)，如果根节点值不相同，
# 则判断pRoot1的左子树和pRoot2是否相同，再判断右子树和pRoot2是否相同
# 3、注意null的条件，HasSubTree中，如果两棵树都不为空才进行判断，is_subtree(self, A, B)中，如果B为空，则说明第二棵树遍历完了，即匹配成功，
# A为空有两种情况，而这两种情况，只需要把B为空的判断放在A为空的判断之前就可以进行处理。
# （1）如果A为空and B不为空说明不匹配，
# （2）如果A为空，B为空，说明匹配。
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:
            return False
        # 不能够这么写，因为会有88792和892这样的案例，即根节点的值和左子树根节点的值相同的情况，
        # if pRoot1.val == pRoot2.val:
        #     return self.is_subtree(pRoot1, pRoot2)
        return self.is_subtree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right,
                                                                                                          pRoot2)

    def is_subtree(self, A, B):
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return self.is_subtree(A.left, B.left) and self.is_subtree(A.right, B.right)


if __name__ == '__main__':
    n1 = TreeNode(8)
    n2 = TreeNode(8)
    n3 = TreeNode(7)
    n4 = TreeNode(9)
    n5 = TreeNode(2)
    n6 = TreeNode(100)
    n7 = TreeNode(100)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    b1 = TreeNode(8)
    b2 = TreeNode(9)
    b3 = TreeNode(2)
    b1.left = b2
    b1.right = b3
    c1 = TreeNode(3)
    c2 = TreeNode(6)
    c1.left = c2
    s = Solution3()
    print(s.HasSubtree(n1, b1))
    # print(s.HasSubtree(n1, c1))
