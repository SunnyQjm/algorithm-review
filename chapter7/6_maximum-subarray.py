#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 53  最大子序和
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#   输入: [-2,1,-3,4,-1,2,1,-5,4],
#   输出: 6
#   解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#
# 进阶:
#   如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
#######################################################################################

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype int

        (knowledge)

        思路：
        1. 使用动态规划；
        2. 定义状态: dp[i] => 表示包含[0, i]区间内包含nums[i]的连续子数组的最大和
        3. 状态转移方程：
            f(i) = nums[0]                              i == 0
                   max{f(i - 1) + nums[i], nums[i]}     i > 0
        """
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1] + nums[i], nums[i])
        return max(nums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), "= 6")

