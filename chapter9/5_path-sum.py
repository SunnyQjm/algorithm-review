#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 112 路径总和
#
# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例: 
#   给定如下二叉树，以及目标和 sum = 22，
#
#              5
#             / \
#            4   8
#           /   / \
#          11  13  4
#         /  \      \
#        7    2      1
#   返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
#######################################################################################


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype bool

        (knowledge)

        思路：
        1. 递归进行先序遍历；
        2. 如果遍历到某个叶子节点，发现路径总和为目标值，则返回True
        """
        if not root:
            return False

        # 找到叶子节点进行判断
        if not root.left and not root.right and root.val == sum:
            return True

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)

    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    print(solution.hasPathSum(root, 22), "= True")

