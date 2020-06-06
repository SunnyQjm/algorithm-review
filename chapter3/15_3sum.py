#!/usr/bin/env python
# coding=utf-8

#########################################################################
# Leetcode 15 三数之和
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 示例：
#   给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
#   满足要求的三元组集合为：
#   [
#     [-1, 0, 1],
#     [-1, -1, 2]
#   ]
#########################################################################


class Solution:
    def threeSum(self, nums):
        """
        
        (Knowledge)

        思路：
        1. 首先对输入的数组进行排序
        2. 从左往右，依次遍历；（遇到和上轮遍历相同的元素直接跳过）
        3. 每次固定当前值，并对当前值右侧的剩余数据执行2sum操作，具体如下：
            - 假设固定值为a，则2sum的目标值(target)为-a；
            - 接着参考前面讨论过的2sum实现执行2sum操作:
              https://github.com/SunnyQjm/algorithm-review/blob/master/chapter1/twoSum.py
                a. 用一个字典记录已经访问过的值及其下标
                b. 如果访问到某个值num[i]是，发现其匹配值target - nums[i] 出现在dict里面，表示其左边有一个是可以与nums[i]想加得target，
                   此时返回[dict[nums[i]], i]即为结果
        4. 过程中使用set对结果集去重，保证没有重复的三元组
        """

        # 特判，过滤掉数组元素不够三个的情况
        if len(nums) < 2:
            return []
        
        # 先对数组进行排序
        nums = sorted(nums)

        result = []

        # 先令first为比第一个值还小的一个值，由于上面执行了排序
        # 所以此时数组中所有的元素都不会等于这个数（第一轮判断的时候就肯定不会跳过）
        first = nums[0] - 1

        # 长度为n的数组，只需要遍历前n-2个数字即可，后面只有两个或者一个数字是无法构成结果要求的三个数字的
        for i in range(len(nums) - 2):

            # 遇到相同的直接跳过（因为每一轮固定一个值，就相当于第一个数为固定值的所有符合条件的三元组都已经添加了）
            if nums[i] == first:
                continue

            # 取当值作为固定值
            first = nums[i]

            # 对固定值右侧的剩余数组进行2sum操作
            # 同时和上面根据first是否相同来跳过一些情况进行剪枝操作一样，也对second和third进行记录和判断，保证结果集不重复
            dict, target, second, third = {}, -first, first - 1, first - 1
            for j in range(i + 1, len(nums)):
                if target - nums[j] == second and nums[j] == third:
                    continue
                if target - nums[j] not in dict:
                    dict[nums[j]] = j
                else:
                    second, third = target - nums[j], nums[j]
                    result.append([first, second, third])
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSum([0, 0, 0]), "= [0, 0, 0]")
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]), "= \n[[-1, 0, 1], [-1, -1, 2]]")
