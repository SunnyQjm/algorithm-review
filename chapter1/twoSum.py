#!/usr/bin/env python
# coding=utf-8


class Solution:

    ################################################
    # 解法一
    ################################################
    def twoSum(self, nums, target):
        """
        (Knowledge)
        1. 对每个值tmp，判断 target - tmp 是否在其右边的剩余数组当中
        2. 如果找到对应的匹配值，则返回两者的位置
        """
        for i in range(len(nums)):
            tmp = nums[i]
            remain = nums[i + 1:]
            if target - tmp in remain:
                return [i, remain.index(target - tmp) + i + 1]

    ################################################
    # 解法2
    ################################################
    def twoSum2(self, nums, target):
        """
        (Knowledge)
        1. 用一个字典记录已经访问过的值及其下标
        2. 如果访问到某个值num[i]是，发现其匹配值target - nums[i] 出现在dict里面，表示其左边有一个是可以与nums[i]想加得target，
           此时返回[dict[nums[i]], i]即为结果
        """
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in dict:
                dict[nums[i]] = i
            else:
                return [dict[target - nums[i]], i]


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum2([2, 7, 11, 15], 9))
