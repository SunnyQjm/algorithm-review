#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 120 三角形最小路径和
#
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
# 相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
#
# 例如，给定三角形：
#   [
#        [2],
#       [3,4],
#      [6,5,7],
#     [4,1,8,3]
#   ]
#   自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
#
# 说明：
#   如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
#######################################################################################


class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype int

        (knowledge)

        思路：
        1. 采用动态规划；
        2. dp[i][j] => 表示triangle[i][j]（i,j从0开始）到达底部所需的最小路径和(这边可以复用triangle作为dp数组)
        3. 状态转移方程：
            f(i, j) = triangle[i][j]                                        j = n - 1
                   triangle[i][j] + min{f(i + 1, j), f(i + 1, j + 1)}       j < n - 1
        """
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]), "= 11")
