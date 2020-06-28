#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 144 二叉树的前序遍历
#
# 给定一个二叉树，返回它的前序遍历。
#
# 示例:
#   输入: [1,null,2,3]  
#      1
#       \
#        2
#       /
#      3 
#
#   输出: [1,2,3]
#
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
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
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype List[int]

        (knowledge)

        思路：
        1. 使用一个列表记录遍历过的值；
        2. 每次先将当前节点的值加入结果集，然后递归遍历左右子树;
        """

        def _preorderTraversal(root, result):
            if not root:
                return result
            result.append(root.val)
            _preorderTraversal(root.left, result)
            _preorderTraversal(root.right, result)
            return result

        result = []
        return _preorderTraversal(root, result)

    def preorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype List[int]

        (knowledge)

        非递归解法
        思路：
        1. 使用一个列表记录遍历过的值；
        2. 每次访问当前值，并将右左子树入栈；
        """
        result, stack = [], [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            result.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        return result
