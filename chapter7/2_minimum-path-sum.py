#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 64 最小路径和
#
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 说明：每次只能向下或者向右移动一步。
#
# 示例:
#   输入:
#   [
#     [1,3,1],
#     [1,5,1],
#     [4,2,1]
#   ]
#   输出: 7
#   解释: 因为路径 1->3->1->1->1 的总和最小。
#######################################################################################


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype int

        (knowledge)

        思路：
        1. 采用动态规划；
        2. dp[i][j] => 表示第i + 1行第j + 1列的网格到右下角网格的最短路径开销(本题可以直接复用grid作为dp数组)
        3. 状态转移方程：
            f(i, j) = grid[i][j]                                        i = m-1 && j = n - 1
                      grid[i][j] + f(i + 1, j)                          i < m - 1 && j = n - 1
                      grid[i][j] + f(i, j + 1)                          i = m - 1 && j < n - 1
                      grid[i][j] + min{f(i + 1, j), f(i, j + 1)}        i < m - 1 && j < n - 1
        """
        m, n = len(grid), len(grid[0])

        # 先处理最右侧一排
        for i in range(m - 2, -1, -1):
            grid[i][n - 1] += grid[i + 1][n - 1]

        # 先处理最底下一行
        for j in range(n - 2, -1, -1):
            grid[m - 1][j] += grid[m - 1][j + 1]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                grid[i][j] += min(grid[i + 1][j], grid[i][j + 1])

        return grid[0][0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]), "= 7")
