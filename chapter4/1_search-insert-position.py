#!/usr/bin/env python
# coding=utf-8

##################################################################################
# Leetcode 35  搜索插入位置
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 你可以假设数组中无重复元素。
#
# 示例 1:
#   输入: [1,3,5,6], 5
#   输出: 2
#
# 示例 2:
#   输入: [1,3,5,6], 2
#   输出: 1
#
# 示例 3:
#   输入: [1,3,5,6], 7
#   输出: 4
#
# 示例 4:
#   输入: [1,3,5,6], 0
#   输出: 0
##################################################################################


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype int

        (knowledge)

        思路：
        1. 用二分查找试图找到目标值；
        2. 找到则返回其索引，没找到则返回其可能被插入的位置
        """
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid
            else:
                left = mid
        return left if nums[left] >= target else (right if nums[right] >= target else right + 1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchInsert([1, 3, 5, 6], 5), "= 2")
    print(solution.searchInsert([1, 3, 5, 6], 2), "= 1")
    print(solution.searchInsert([1, 3, 5, 6], 7), "= 4")
    print(solution.searchInsert([1, 3, 5, 6], 0), "= 0")
