#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 257 二叉树的所有路径
#
# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
#   输入:
#
#      1
#    /   \
#   2     3
#    \
#     5
#
#   输出: ["1->2->5", "1->3"]
#
#   解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
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
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype List[str]

        (knowledge)

        思路：
        1. 递归的进行先序遍历，过程中记录走过的路径；
        2. 当遍历到一个叶子节点时，将当前路径添加到结果集当中；
        """
        def preorderTraversal(root, s, result):
            if not root:
                return
            if not root.left and not root.right:
                result.append(s + "->" + str(root.val))
            preorderTraversal(root.left, s + "->" + str(root.val), result)
            preorderTraversal(root.right, s + "->" + str(root.val), result)

        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        s = str(root.val)
        result = []
        preorderTraversal(root, s, result)
        return result

