#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 263 丑数
# 
# 编写一个程序判断给定的数是否为丑数。
# 丑数就是只包含质因数 2, 3, 5 的正整数。
#
# 示例 1:
#   输入: 6
#   输出: true
#   解释: 6 = 2 × 3
#
# 示例 2:
#   输入: 8
#   输出: true
#   解释: 8 = 2 × 2 × 2
#
# 示例 3:
#   输入: 14
#   输出: false 
#   解释: 14 不是丑数，因为它包含了另外一个质因数 7。
#######################################################################################

class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype bool

        (knowledge)

        思路：
        1. 依次判断能否用2, 3, 5整除，可以则将num处理对应质因子；
        2. 判断最后结果是否为1
        """
        if num == 0:
            return False
        while not num % 5:
            num /= 5
        while not num % 3:
            num /= 3
        while not num % 2:
            num /= 2
        return num == 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.isUgly(6), "= True")
    print(solution.isUgly(8), "= True")
    print(solution.isUgly(14), "= False")
