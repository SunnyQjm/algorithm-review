#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 111 二叉树的最小深度
#
# 给定一个二叉树，找出其最小深度。
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
#   给定二叉树 [3,9,20,null,null,15,7],
#
#       3
#      / \
#     9  20
#       /  \
#      15   7
#   返回它的最小深度  2.
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
    def minDepth(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype int

        (knowledge)

        思路：
        1. 通过DFS递归遍历目标树，一旦遍历到叶子节点，马上返回
        """
        if root is None:
            return 0

        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        return max(self.minDepth(root.left), self.minDepth(root.right)) + 1


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(solution.minDepth(root), "= 2")
