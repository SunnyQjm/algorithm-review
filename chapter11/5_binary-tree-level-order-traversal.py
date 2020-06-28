#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 102 二叉树的层序遍历
#
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
# 
# 示例：
#   二叉树：[3,9,20,null,null,15,7],
#
#       3
#      / \
#     9  20
#       /  \
#      15   7
#   返回其层次遍历结果：
#
#   [
#     [3],
#     [9,20],
#     [15,7]
#   ]
#######################################################################################

from typing import List
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        if self:
            return "{}->{}->{}".format(self.val, repr(self.left), repr(self.right))


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        :type root: TreeNode
        :rtype List[List[int]]

        (knowledge)

        思路：
        1. 采用图的BFS遍历的思想对树进行逐层遍历；
        2. 用queue来实现BFS；（由于这边是树型结构，所以不会有环路，故不需要用visited来记录哪些节点已经访问过）
        3. 为了记录当前遍历的节点在哪一层，我们用两个变量curLevelNum和nextLevelNum来分别记录当前层次还有多少没有遍历，以及下一层次还有多少没有遍历

        tip: ppt中用的是DFS的方法，那种方法可以更容易的记录当前节点所属层级
        """

        # 特判树为空的情况
        if not root:
            return []

        # 初始时curLevelNum = 1表示要遍历的第一层为根节点只有一个
        # 初始时nextLevelNum = 0，当遍历节点时，会增加下一层的可遍历节点数量
        curLevelNum, nextLevelNum = 1, 0
        result = [[]]
        queue = collections.deque([root])

        while queue:
            curNode = queue.popleft()
            result[-1].append(curNode.val)
            curLevelNum -= 1

            # 判断当前节点的左右节点是否存在，存在则入队
            if curNode.left:
                queue.append(curNode.left)
                nextLevelNum += 1
            if curNode.right:
                queue.append(curNode.right)
                nextLevelNum += 1

            if curLevelNum == 0:  # 判断是否换层
                curLevelNum, nextLevelNum = nextLevelNum, 0
                # 如果下一层还有可遍历的节点，则往结果集里面新加一个空列表用来存储下一层的遍历结果
                if curLevelNum != 0:
                    result.append([])

        return result


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(solution.levelOrder(root), "= [[3], [9, 20], [15, 7]]")
