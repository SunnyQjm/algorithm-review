#!/usr/bin/env python
# coding=utf-8

###############################################################
# Leetcode 70
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 注意：给定 n 是一个正整数。
#
# 示例 1：
#   输入： 2
#   输出： 2
#   解释： 有两种方法可以爬到楼顶。
#   1.  1 阶 + 1 阶
#   2.  2 阶
#
# 示例 2：
#   输入： 3
#   输出： 3
#   解释： 有三种方法可以爬到楼顶。
#   1.  1 阶 + 1 阶 + 1 阶
#   2.  1 阶 + 2 阶
# 　 3.  2 阶 + 1 阶
###############################################################

class Solution:
    def climbingStairs(self, n):
        """
        (Knowledge)

        思路：
        1. 想要到第n个台阶，可以从n-1层爬一个台阶到达，或者从n-2层爬两个台阶到达;
        
        2. 令f(n)位到达第n个台阶的方法数，则有：f(n) = f(n - 1) + f(n - 2)  => 状态转移方程

        3. 由于从下往上计算到达每个台阶的方法数时，只需要前两个台阶的方法数，所以只需要用两个变量保存状态即可
        """
        pre, cur = 0, 1
        for i in range(n):
            pre, cur = cur, pre + cur
        return cur


if __name__ == '__main__':
    solution = Solution()
    print(solution.climbingStairs(2))
    print(solution.climbingStairs(3))
    print(solution.climbingStairs(4))
