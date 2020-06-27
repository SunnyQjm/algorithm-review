#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# 背包问题
#
# 给你一个可装载重量为 W 的背包和 N 个物品，每个物品有重量和价值两个属性。其中第 i 个
# 物品的重量为wt[i]，价值为 val[i]，现在让你用这个背包装物品，最多能装的价值是多少？
#
#######################################################################################

class Solution:
    def knapsack(self, W, N, wt, val):
        """
        :type W:int
        :type N:int
        :type wt:[int]
        :type val:[int]
        :rtype int

        思路：
        1. 使用动态规划；
        2. 定义状态：dp[i][w] => 表示只放前i个物品，且背包容量为w的情况下，最多能装的价值；
        3. base case => dp[0][...]和dp[...][0]都应该为0，表示没有物品可放或者背包容量为0的情况下，能装的价值自然为0；
        4. 状态转移方程：
            f(i, w) = 0                                                         i == 0 || w == 0
                    = f(i - 1, w)                                               i > 0 && w > 0 && wt[i] > w      => 如果一个物品的重量都大于背包的重量了，肯定不能放进背包
                    = max{f(i - 1, w), f(i - 1, w - wt[i]) + val[i]}            i > 0 && w > 0 && wt[i] <= w     => 根据放或者不放第i个物品，取最大价值   

        tip: 可以参考 => https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/bei-bao-wen-ti
        """
        dp = [[0] * (W + 1) for i in range(N + 1)]
        for i in range(1, N + 1):
            for w in range(1, W + 1):
                if wt[i - 1] > w:
                    dp[i][w] = dp[i - 1][w]
                else:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - wt[i - 1]] + val[i - 1])
        return dp[N][W]


if __name__ == '__main__':
    solution = Solution()
    print(solution.knapsack(4, 3, [2, 1, 3], [4, 2, 3]), "= 6")

