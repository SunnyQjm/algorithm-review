#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 100 相同的树
#
# 给定两个二叉树，编写一个函数来检验它们是否相同。
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
# 
# 示例 1:
#   输入:       1         1
#              / \       / \
#             2   3     2   3
#
#            [1,2,3],   [1,2,3]
#
#   输出: true
#
# 示例 2:
#   输入:      1          1
#              /           \
#             2             2
#
#            [1,2],     [1,null,2]
#
#   输出: false
#
# 示例 3:
#   输入:       1         1
#              / \       / \
#             2   1     1   2
#
#            [1,2,1],   [1,1,2]
#
#   输出: false
#######################################################################################


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype bool

        (knowledge)
        
        思路：
        1. 判断当前两个根节点的值是否相等，不相等则返回false
        2. 递归判断对应的左子树和右子树是否相等
        """
        if not p or not q:
            if not q and not p:
                return True
            else:
                return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    solution = Solution()
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    print(solution.isSameTree(p, q), "= True")

    p = TreeNode(1)
    p.left = TreeNode(2)

    q = TreeNode(1)
    q.right = TreeNode(2)
    print(solution.isSameTree(p, q), "= False")
