#!/usr/bin/env python
# coding=utf-8

###############################################################
# Leetcode 66  加一
#   https://leetcode-cn.com/problems/plus-one/
# 
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
# 示例 1:
#   输入: [1,2,3]
#   输出: [1,2,4]
#   解释: 输入数组表示数字 123。
#
# 示例 2:
#   输入: [4,3,2,1]
#   输出: [4,3,2,2]
#   解释: 输入数组表示数字 4321。
###############################################################


from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """

        (Knowledge)

        算法思路：
        1. 从最末尾开始遍历；
        2. 对当前元素+1，不足10则结束，满10则执行进位
            => 进位就将当前元素值置为0,然后下标左移，继续判断

        3. 如果遍历到头元素了还有进位，则需要在头元素之前插入一个元素，值为1
        """

        # 特判空数组的情况
        if len(digits) == 0:
            return [1]
 
        needAdd = False
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
                needAdd = True
            else:
                needAdd = False
                break

        if needAdd:
            digits.insert(0, 1)
        
        return digits



if __name__ == '__main__':
    solution = Solution()

    print(solution.plusOne([1, 2, 3]), "= [1, 2, 4]")
    print(solution.plusOne([4, 3, 2, 1]), "= [4, 3, 2, 2]")
    print(solution.plusOne([9, 9, 9]), "= [1, 0, 0, 0]")
    print(solution.plusOne([9]), "= [1, 0]")
    print(solution.plusOne([8, 9, 9, 9]), "= [9, 0, 0, 0]")

