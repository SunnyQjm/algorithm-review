#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 300 最长上升子序列
#
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
#
# 示例:
#   输入: [10,9,2,5,3,7,101,18]
#   输出: 4 
#   解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
#
# 说明:
#   可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
#   你算法的时间复杂度应该为 O(n2) 。
#
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
#######################################################################################

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype int

        (knowledge)

        思路：
        nums => size = n
        1. 采用动态规划的思想；
        2. dp[i] => 表示[i:n-1]范围内的最长的上升子序列的长度；
        3. 状态转移方程：
            f(i) = 1                                                i == n - 1
                   1 + max{f(j) | nums[j] > nums[i] && i < j < n}   i < n - 1
        """
        if not nums:
            return 0
        length = len(nums)
        dp, result = [1 for i in range(length)], 1

        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), "= 4")

