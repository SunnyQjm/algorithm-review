#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 934 最短的桥
#
# 在给定的二维二进制数组 A 中，存在两座岛。（岛是由四面相连的 1 形成的一个最大组。）
# 现在，我们可以将 0 变为 1，以使两座岛连接起来，变成一座岛。
# 返回必须翻转的 0 的最小数目。（可以保证答案至少是 1。）
#
# 示例 1：
#   输入：[[0,1],[1,0]]
#   输出：1
#
# 示例 2：
#   输入：[[0,1,0],[0,0,0],[0,0,1]]
#   输出：2
#
# 示例 3：
#   输入：[[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
#   输出：1
#
# 提示：
#   1. 1 <= A.length = A[0].length <= 100
#   2. A[i][j] == 0 或 A[i][j] == 1
#######################################################################################

from typing import List


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        """
        :type A: List[List[int]]
        :rtype int

        (knowledge)

        思路：
        1. 首先使用DFS的方式找到其中一座岛屿，并将该岛屿内所有块标记为2；
        2. 接着使用BFS的方式逐层向外探索：
            - 超出边界则忽略；
            - 探索到海域，则将其标记为2，表示已经探索过；
            - 当探索到1即终止，返回当前的轮数
        """
        n, queue = len(A), []

        def dfs(i, j, queue):
            if i < 0 or j < 0 or i >= n or j >= n or A[i][j] != 1:
                return
            A[i][j] = 2
            queue.append((i, j))
            dfs(i - 1, j, queue)
            dfs(i + 1, j, queue)
            dfs(i, j - 1, queue)
            dfs(i, j + 1, queue)
            return

        # 通过dfs找到第一座岛屿
        find = False
        for i in range(n):
            for j in range(n):
                if A[i][j] == 1:
                    dfs(i, j, queue)
                    find = True
                    break
            if find:
                break

        # 通过BFS搜索另一个岛屿
        s = 0  # 轮数
        while queue:
            for _ in range(len(queue)):
                i, j = queue.pop(0)
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    x, y = i + dx, j + dy
                    if x < 0 or y < 0 or x >= n or y >= n or A[x][y] == 2:
                        continue
                    if A[x][y] == 1:
                        return s

                    # 经过海域，则将其标记为2,表示已经探索过
                    A[x][y] = 2
                    queue.append((x, y))
            s += 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.shortestBridge([[0, 1], [1, 0]]), "= 1")
    print(solution.shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]]), "= 2")
    print(
        solution.shortestBridge([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]),
        "= 1")
