#!/usr/bin/env python
# coding=utf-8

###################################################################################
# Leetcode 50 Pow(x, n)
#   https://leetcode-cn.com/problems/powx-n/
#
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
#
# 示例 1:
#   输入: 2.00000, 10
#   输出: 1024.00000
#
# 示例 2:
#   输入: 2.10000, 3
#   输出: 9.26100
#
# 示例 3:
#   输入: 2.00000, -2
#   输出: 0.25000
#   解释: 2-2 = 1/22 = 1/4 = 0.25
#
# 说明:
#   -100.0 < x < 100.0
#   n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
###################################################################################

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float

        (knowledge)

        思路：
        1. 使用递归的方式计算，结束条件位n=0;
        2. 对于n的不同情况，分别处理：
            - n < 0的情况下，求x^|n|再倒数一下就可；
            - n 为奇数的情况下，直接递归一层；
            - n 为偶数的情况下，可以剪枝，x^(2m) = (x * x)^m
        """

        # 结束条件 n = 0
        if not n:
            return 1

        # 处理n为负数的情况
        if n < 0:
            return 1 / self.myPow(x, -n)

        # 处理n为奇数的情况
        if n % 2:
            return x * self.myPow(x, n - 1)

        # 处理n为偶数的情况
        return self.myPow(x * x, n / 2)


if __name__ == '__main__':
    solution = Solution()
    print(solution.myPow(2, 10), "= 1024")
    print(solution.myPow(2.1, 3), "= 9.261")
    print(solution.myPow(2, -2), "= 0.25")
