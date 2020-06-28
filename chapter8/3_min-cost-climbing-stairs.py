#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 746  使用最小花费爬楼梯
#
# 数组的每个索引作为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
# 每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
# 您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。
#
# 示例 1:
#   输入: cost = [10, 15, 20]
#   输出: 15
#   解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
#
# 示例 2:
#   输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
#   输出: 6
#   解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
#
# 注意：
#   1. cost 的长度将会在 [2, 1000]。
#   2. 每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。
#######################################################################################


class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int

        思路：
            题目中其实cost[i]表示如果要站在第i个阶梯上，需要付出的代价，然后隐含了一个楼层顶部其实是一个代价为0的虚拟阶梯
        1. 使用动态规划；
        2. 定义状态：dp[i] => 到达第i个台阶所需的最小花费；（i从0~len(cost)）
        3. base case => dp[0] = cost[0], dp[1] = cost[1]
        4. 状态转移方程：
            f(i) = cost[i]                                                  i == 0 || i == 1
                   cost[i] + min{cost[i - 1], cost[i - 2]}                  i > 1
        """

        # 最末尾添加一个开销为0的虚拟阶梯，代表楼顶，我们的目标就是要到达这个楼顶
        cost.append(0)
        for i in range(2, len(cost)):
            cost[i] = cost[i] + min(cost[i - 1], cost[i - 2])
        return cost[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minCostClimbingStairs([10, 15, 20]), "= 15")
    print(solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), "= 6")
