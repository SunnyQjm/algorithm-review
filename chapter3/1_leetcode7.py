#!/usr/bin/env python
# coding=utf-8

##############################################################
# Leetcode 7 整数反转
#   https://leetcode-cn.com/problems/reverse-integer/ 
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1:
#   输入: 123
#   输出: 321
#
# 示例 2:
#   输入: -123
#   输出: -321
#
# 示例 3:
#   输入: 120
#   输出: 21
#
##############################################################

INT_MAX_VAL = 2147483647
INT_MIN_VAL = -2147483648

class Solution:
    def reverse(self, x):
        """
        (Knowledge)

        思路：
        1. 首先记录输入值的符号（是正数还是负数），然后取其绝对值|x|进行处理
        2. 接着用一个long型（Python里面的数字完全够大）存储结果；
        3. 将|x|从个位开始向左遍历，依次叠加到结果里面；
        4. 最后判断结果是否移出（与32位有符号整形的最大值和最小值进行比对）
        """
        isNegitive = -1 if x < 0 else 1
        result, x = 0, abs(x)
        while x > 0:
            result = result * 10 + x % 10
            x = x // 10
        result = isNegitive * result

        return 0 if result > INT_MAX_VAL or result < INT_MIN_VAL else result


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(123), "= 321")
    print(solution.reverse(-123), "= -321")
    print(solution.reverse(120), "= 21")
