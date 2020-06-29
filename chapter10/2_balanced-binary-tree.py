#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 110 平衡二叉树
#
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 本题中，一棵高度平衡二叉树定义为：
#   一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
#
# 示例 1:
#   给定二叉树 [3,9,20,null,null,15,7]
#
#       3
#      / \
#     9  20
#       /  \
#      15   7
#   返回 true 。
#
# 示例 2:
#   给定二叉树 [1,2,2,3,3,null,null,4,4]
#
#          1
#         / \
#        2   2
#       / \
#      3   3
#     / \
#    4   4
#   返回 false。
#######################################################################################


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        if self:
            return "{}->{}->{}".format(self.val, repr(self.left), repr(self.right))


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype bool

        (knowledge)

        思路：
        1. 直接递归计算每个节点左右子树的高度;
        2. 根据AVL树的特性，如果任意一个节点的左右子树的高度差大于一，则该树不是AVL树，标记器高度为-1;
        3. 如果某个子树的高度计算为-1,则表示该子树不是AVL树，-1会一直传递到顶层。
        """

        def preOrderTraversal(root):
            if not root:
                return 0
            leftNum = preOrderTraversal(root.left)
            rightNum = preOrderTraversal(root.right)
            if leftNum == -1 or rightNum == -1 or abs(leftNum - rightNum) > 1:
                return -1
            return 1 + max(leftNum, rightNum)

        return preOrderTraversal(root) != -1
