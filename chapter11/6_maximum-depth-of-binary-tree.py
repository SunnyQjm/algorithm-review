#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 104 二叉树的最大深度
#
# 给定一个二叉树，找出其最大深度。
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例：
#   给定二叉树 [3,9,20,null,null,15,7]，
#
#       3
#      / \
#     9  20
#       /  \
#      15   7
#   返回它的最大深度 3 。
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
    def maxDepth(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype int

        (knowledge)

        思路：
        1. 使用先序方法遍历，在遍历过程中传递当前层级深度；
        2. 使用递归方式实现
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(solution.maxDepth(root), "= 3")
