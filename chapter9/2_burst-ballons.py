#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 312 戳气球
# 
# 有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
# 现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i
# 后，气球 left 和气球 right 就变成了相邻的气球。
#
# 求所能获得硬币的最大数量。
#
# 说明:
#   - 你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
#   - 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
#
# 示例:
#   输入: [3,1,5,8]
#   输出: 167 
#   解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#         coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
#######################################################################################


class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype int

        (knowledge)

        思路：
        1. 根据题意，我们在数组的左右各加一个元素，代表不能被戳破的假气球，其值为1，此时气球的编号为0~n+1(首尾两个气球不能戳破，1~n号气球对应题目中的编号0~n-1)；
        2. 使用动态规划；
        3. 定义状态：dp[i][j] => 戳破编号i和编号j（开区间，不包括编号为i和编号为j的气球）之间的所有气球所能获得硬币的最大数量；
        4. base case => dp[i][j] = 0 (i <= j <= i + 1), 由于状态定义的时候是开区间，所以i <= j <= i + 1时，dp[i][j]表示没有气球可以被戳破，所以为0；
        5. 状态转移方程：
            f(i, j) = 0                                                                         i <= j <= i + 1
                      min{f(i, k) + f(k, j) + nums[i] * nums[k] * nums[j] | i < k < j}          j > i + 1



        如何确定遍历顺序呢？
        tip：参考 =>    https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/za-qi-qiu
        """
        length = len(nums)

        # 在前后各添加一个不能戳破的假气球，其值为1
        nums.insert(0, 1)
        nums.append(1)

        # 初始化dp数组
        dp = [[0] * (length + 2) for i in range(length + 2)]

        for i in range(2, length + 2):
            for j in range(0, length + 2 - i):
                dp[j][j + i] = max(
                    (dp[j][k] + dp[k][j + i] + nums[j] * nums[k] * nums[j + i]) for k in range(j + 1, j + i))

        return dp[0][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxCoins([3, 1, 5, 8]), "= 167")
