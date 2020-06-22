#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 105 从前序与中序遍历序列构造二叉树
#
# 根据一棵树的前序遍历与中序遍历构造二叉树。
#
# 注意:
#   你可以假设树中没有重复的元素。
#
# 例如，给出
#   前序遍历 preorder = [3,9,20,15,7]
#   中序遍历 inorder = [9,3,15,20,7]
#
# 返回如下的二叉树：
#       3
#      / \
#     9  20
#       /  \
#      15   7
#######################################################################################

from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        if self:
            return "{}->{}->{}".format(self.val, repr(self.left), repr(self.right))


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype TreeNode

        (knowledge)

        思路：
        1. 首先根据中序定位根节点；                 
            3 9 20 15 7
            _

        2. 然后根据先序，划分左右子树；
            9 3 15 20 7
              _
        
        3. 然后将左右子树部分各自递归的进行构建即可
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        
        # 用于记录左右子树的元素个数
        leftNum, rightNum = 0, 0

        for num in inorder:
            if num == preorder[0]:
                break
            leftNum += 1

        root.left = self.buildTree(preorder[1:1+leftNum], inorder[0:leftNum])
        root.right = self.buildTree(preorder[1+leftNum:], inorder[leftNum + 1:])
        return root


if __name__ == '__main__':
    solution = Solution()
    solution.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
