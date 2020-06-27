#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 63 不同路径 II
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
#
# 说明：m 和 n 的值均不超过 100。
#
# 示例 1:
#
#   输入:
#   [
#     [0,0,0],
#     [0,1,0],
#     [0,0,0]
#   ]
#   输出: 2
#   解释:
#   3x3 网格的正中间有一个障碍物。
#   从左上角到右下角一共有 2 条不同的路径：
#   1. 向右 -> 向右 -> 向下 -> 向下
#   2. 向下 -> 向下 -> 向右 -> 向右
#######################################################################################

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype int

        (knowledge)

        思路：
        1. 动态规划
        2. dp[i][j] => 第处于第i + 1行第j + 1列的方格，到目的地可走的路径数量
        3. 状态转移方程：
            f(i, j) = f(i + 1, j) + f(i, j + 1)    i+1 < m && j+1 < n && obstacleGrid[i][j] != 1
                      f(i + 1, j)                  i+1 < m && j+1 == n && obstacleGrid[i][j] != 1
                      f(i, j + 1)                  i+1 == m && j+1 < n && obstacleGrid[i][j] != 1
                      0                            (i+1 == m && j+1 == n) || obstacleGrid[i][j] == 1
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for i in range(m)]
        dp[m - 1][n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                    continue
                if i + 1 < m:
                    dp[i][j] += dp[i + 1][j]
                if j + 1 < n:
                    dp[i][j] += dp[i][j + 1]
        return dp[0][0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), "= 2")

