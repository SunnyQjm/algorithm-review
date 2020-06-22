#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 235 二叉搜索树的最近公共祖先
#
# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
# 
# 例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]
#           6
#         /   \
#        2     8
#       / \   / \
#      0   4 7   9
#         / \
#        3   5
#
# 示例 1:
#   输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
#   输出: 6 
#   解释: 节点 2 和节点 8 的最近公共祖先是 6。
#
# 示例 2:
#   输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
#   输出: 2
#   解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
#
# 说明:
#   - 所有节点的值都是唯一的。
#   - p、q 为不同节点且均存在于给定的二叉搜索树中。
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
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype TreeNode

        (knowledge)

        思路：
        1. 直接根据二叉搜索树的性质，对树进行先序遍历；
        2. 将两个目标节点根据节点值得大小，小的指定为left， 大的指定为right
        2. 如果找到一个节点，其值大于等于left.val，且小于等于right.val，则该节点即为要求的结果
        3. 如果当前节点不是目标节点，则对左右子树进行递归遍历
        """
        def preOrderTraversal(root, left, right):
            if not root or (left.val <= root.val <= right.val):
                return root

            leftResult = preOrderTraversal(root.left, left, right)
            rightResult = preOrderTraversal(root.right, left, right)
            return leftResult if not rightResult else rightResult

        left = p if p.val < q.val else q
        right = p if p.val >= q.val else q
        return preOrderTraversal(root, left, right)


