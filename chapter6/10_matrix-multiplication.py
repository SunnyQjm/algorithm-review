#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# 矩阵相乘 => 详情见PPT
#
# 描述：设 A1, A2, … , An 为矩阵序列，Ai 为Pi-1xPi 阶矩阵，i = 1,2,…,n. 确定乘法顺序使得元素相乘的总次数最少.
# 输入：向量 P = <P0, P1, … , Pn>，n个矩阵的行数、列数
#
# 实例：P = <10, 100, 5, 50>
#       A1: 10x100, A2: 100x5, A3: 5x50
# 括号位置不同，相乘总次数不同：
#       (A1 A2)A3: 10x100x5 + 10x5x50 = 7500
#       A1(A2 A3): 10x100x50 + 100x5x50 = 75000
#######################################################################################

class Solution:
    def miniMultiplicationTimes(self, matrixs):
        """
        :type matrixs: List[int]
        :rtype int

        (knowledge)

        思路：
        1. 使用动态规划；
        2. dp[i][j] => 得到Ai..j 所需要的最少相乘次数
        3. 状态转移方程：
           m(i, j) = 0                                                  i <= j <= i + 1
                     min(i < k < j){m(i, k) + m(k, j) + Pi*Pk*Pj}       j > i + 1
        """
        
        # 初始化dp数组
        dp = [[float("inf") for i in range(len(matrixs))] for i in range(len(matrixs))]

        # 让满足 i <= j <= i + 1的置为0
        for i in range(len(matrixs) - 1):
            dp[i][i] = 0
            dp[i][i + 1] = 0
        dp[len(matrixs) - 1][len(matrixs) - 1] = 0

        # 此处i表示每轮要求的目标值的间隔
        # 比如i=2，表示求所有索引间隔为2得dp值，eg.: dp[0][2], dp[1][3], dp[2][4]...
        for i in range(2, len(matrixs)):
            for j in range(len(matrixs) - i):
                for k in range(j + 1, j + i):
                    dp[j][j + i] = min(dp[j][j + i], dp[j][k] + dp[k][j + i] + matrixs[j] * matrixs[k] * matrixs[j + i])
        return dp[0][len(matrixs) - 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.miniMultiplicationTimes([30, 35, 15, 5, 10, 20]), "= 11875")
