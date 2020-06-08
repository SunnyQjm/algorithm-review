#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 123 买卖股票的最佳时机 III
#
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
# 示例 1:
#   输入: [3,3,5,0,0,3,1,4]
#   输出: 6
#   解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
#         随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
#
# 示例 2:
#   输入: [1,2,3,4,5]
#   输出: 4
#   解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
#         注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
#         因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
#
# 示例 3:
#   输入: [7,6,4,3,1] 
#   输出: 0 
#   解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
#######################################################################################

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype int

        (knowledge)

        思路：
        prices => size = n
        1. 首先，反向遍历一遍，算出[i:n-1]（i的取值位0~n-1）范围内完成一次交易最多可得多少收益
            - dp[i] => 第i天到最后一天的范围内，完成一次交易最多可以获得的收益
            - maxV => 在反向遍历过程中，记录的已遍历部分的最高价格
            - 状态转移方程：
                dp[i] = 0                                   i == n - 1
                      = max(dp[i + 1], max - prices[i])     i < n - 1
        2. 接着进行正向遍历, 计算[0:i]范围内完成一次交易最多可得多少收益：
            - min => 记录在正向遍历过程中，已遍历部分的最低价格
            - last => 记录[0:i-1]范围内完成一次交易最多可得多少收益
            - 状态转移方程：
                cur = 0                                     i == 0
                      max(last, prices[i] - min)            i > 0
        3. 在正向遍历过程中，通过查询第一步的dp表，可以知道两次交易的收益和，记录最大值
        """
        if not prices:
            return 0

        length = len(prices)

        # 反向遍历初始化(可以只交易一次，第二次不交易，所以dp数组要比length+1,并且最后一个元素值为0,代表不做交易)
        dp = [0 for i in range(length + 1)]
        dp[length - 1], maxV = 0, prices[length - 1]

        # 反向遍历
        for i in range(len(prices) - 1, -1, -1):
            dp[i] = max(dp[i + 1], maxV - prices[i])
            if prices[i] > maxV:
                maxV = prices[i]

        # 正向遍历初始化
        last, min, result = 0, prices[0], 0
        for i in range(1, len(prices)):
            cur = max(last, prices[i] - min)
            last, result = cur, max(result, cur + dp[i + 1])
            if prices[i] < min:
                min = prices[i]

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]), "= 6")
    print(solution.maxProfit([1, 2, 3, 4, 5]), "= 4")
    print(solution.maxProfit([7, 6, 4, 3, 1]), "= 0")

