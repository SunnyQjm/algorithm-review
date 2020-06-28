#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 62 不同路径
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 问总共有多少条不同的路径？
#
# 示例 1:
#   输入: m = 3, n = 2
#   输出: 3
#   解释:
#   从左上角开始，总共有 3 条路径可以到达右下角。
#   1. 向右 -> 向右 -> 向下
#   2. 向右 -> 向下 -> 向右
#   3. 向下 -> 向右 -> 向右
#
# 示例 2:
#   输入: m = 7, n = 3
#   输出: 28
#######################################################################################


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype int

        (knowledge)

        思路：
        1. 采用动态规划
        2. dp[i][j] => 第处于第i + 1行第j + 1列的方格，到目的地可走的路径数量
        3. 状态转移方程：
            f(i, j) = f(i + 1, j) + f(i, j + 1)    i+1 < m && j+1 < n
                      f(i + 1, j)                  i+1 < m && j+1 == n
                      f(i, j + 1)                  i+1 == m && j+1 < n
                      0                            i+1 == m && j+1 == n
        """
        dp = [[0 for i in range(n)] for i in range(m)]
        dp[m - 1][n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + 1 < m:
                    dp[i][j] += dp[i + 1][j]
                if j + 1 < n:
                    dp[i][j] += dp[i][j + 1]
        return dp[0][0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePaths(3, 2), "= 3")
    print(solution.uniquePaths(7, 3), "= 28")
