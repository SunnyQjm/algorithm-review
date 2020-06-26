#!/usr/bin/env python
# coding=utf-8

##############################################################################
# Leetcode 16 最接近的三数之和
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 示例：
#   输入：nums = [-1,2,1,-4], target = 1
#   输出：2
#   解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#
# 提示：
#   3 <= nums.length <= 10^3
#   -10^3 <= nums[i] <= 10^3
#   -10^4 <= target <= 10^4
##############################################################################

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype int

        (Knowledge)

        思路：
        1. 采用类似3sum的方法；
        2. 首先对输入的数组进行排序；
        3. 接着固定一个数，对固定数右侧的剩余数组使用双指针进行遍历，过程中只保存最接近target的值；
        4. 同时对已经遍历过的相同数字进行跳过，达到剪枝的目的

        PS: 这种方法可以AC，但是耗时较长，大概4000ms左右(但是思路比较简单直观)
        """
        # 先对数组进行排序
        nums, result, miniGap = sorted(nums), nums[0] + nums[1] + nums[2], abs(target - (nums[0] + nums[1] + nums[2]))

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

            second = first - 1
            for j in range(i + 1, len(nums) - 1):
                if nums[j] == second:
                    continue
                second = nums[j]
                third = second - 1

                for k in range(j + 1, len(nums)):
                    if nums[k] == third:
                        continue
                    third = nums[k]
                    tmp = first + second + third
                    if abs(target - tmp) < miniGap:
                        result, miniGap = tmp, abs(target - tmp)
        return result

    def threeSumClosest2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype int

        (Knowledge)

        思路：
        1. 首先对输入的数组进行排序；
        2. 接着固定一个数，对固定数右侧的剩余数组使用双指针进行遍历，期间考虑数组有序通过移动指针逼近target；
        3. 同时对已经遍历过的相同数字进行跳过，达到剪枝的目的

        PS: 本解法性能更优，耗时68ms左右，只要理解如何利用双指针逼近target即可：
            此处有图解 => https://leetcode-cn.com/problems/3sum-closest/solution/hua-jie-suan-fa-16-zui-jie-jin-de-san-shu-zhi-he-b/
        """
        # 先对数组进行排序
        nums, result, miniGap = sorted(nums), nums[0] + nums[1] + nums[2], abs(target - (nums[0] + nums[1] + nums[2]))

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
            left, right = i + 1, len(nums) - 1
            while left < right:
                tmp = first + nums[left] + nums[right]
                if abs(target - tmp) < miniGap:
                    result, miniGap = tmp, abs(target - tmp)
                if tmp < target:
                    left += 1
                elif tmp > target:
                    right -= 1
                else:
                    return tmp
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSumClosest([-3, -2, -5, 3, -4], -1), "= -2")
    print(solution.threeSumClosest([0, 1, 2], 0), "= 3")
    print(solution.threeSumClosest([1, 1, 1, 1], 0), "= 3")
    print(solution.threeSumClosest([-1, 2, 1, -4], 1), "= 2")

    print(solution.threeSumClosest2([-3, -2, -5, 3, -4], -1), "= -2")
    print(solution.threeSumClosest2([0, 1, 2], 0), "= 3")
    print(solution.threeSumClosest2([1, 1, 1, 1], 0), "= 3")
    print(solution.threeSumClosest2([-1, 2, 1, -4], 1), "= 2")
