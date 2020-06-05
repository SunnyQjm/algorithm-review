#!/usr/bin/env python
# coding=utf-8


################################################################
# LeetCode: 69 Sqrt(x)
# Implement int sqrt(int x).
# Compute and return the square root of x, where x is guaranteedto be a non-negative integer.
# Since the return type is an integer, the decimal digits aretruncated and only the integer part of the result is returned.
################################################################

import math

class Solution:
    def mySqrt(self, x):
        """
        (Knowledge)

        函数功能描述: 传入一个数字，返回其平方根的整数部分

        思路：
        1. 首先用特判，处理掉x=1的特殊情况；
        2. 接着用二分法，找到x平方根的整数部分；

        二分法的结束条件：跳出循环之前的最后一次循环，left == right, 此时得到 mid == left，因此：
            
            - 如果mid > x * mid，则 x 的平方根必然为比left略小一点的某个值，所以最后结果返回 left - 1
            
            - 如果mid <= x * mid, 则 x 的平方根必然为比left略大一点某个值，又因为执行了 left = mid +１, 所以最后结果返回 left - 1
            
        """
        if x < 2:
            return x
        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            if mid > x / mid:
                right = mid - 1
            else:
                left = mid + 1
        return left - 1

    def mySqrt2(self, x):
        """
        (Knowledge)

        算法说明：使用牛顿迭代法，近似求平方根
        牛顿迭代法求平方跟的证明详见 => https://www.cnblogs.com/upcan/p/9907402.html

        最终得到迭代公式： next = 1/2 * (next + input / next)
            - next => 等式左边为下一个近似值，等式右的next表示上一个近似值
            - input => 输入值
        """

        # 首先猜测一个初始的预测值
        next = x / 2

        # 运行20次迭代（这个迭代次数取决于需要的精度，迭代次数越多，得到的结果越精确）
        for k in range(20):
            next = 1 / 2 * (next + x / next)

        # 根据题意，进行向下取整
        return math.floor(next)



if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt(9))
    print(solution.mySqrt(8))
    print(solution.mySqrt(10))
    print(solution.mySqrt(7))
    print(solution.mySqrt2(9))
    print(solution.mySqrt2(8))
    print(solution.mySqrt2(10))
    print(solution.mySqrt2(7))
