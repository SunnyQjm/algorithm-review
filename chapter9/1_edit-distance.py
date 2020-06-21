#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 72 编辑距离
#
# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
# 你可以对一个单词进行如下三种操作：
#   1. 插入一个字符
#   2. 删除一个字符
#   3. 替换一个字符
#
# 示例 1：
#   输入：word1 = "horse", word2 = "ros"
#   输出：3
#   解释：
#   horse -> rorse (将 'h' 替换为 'r')
#   rorse -> rose (删除 'r')
#   rose -> ros (删除 'e')
#
# 示例 2：
#   输入：word1 = "intention", word2 = "execution"
#   输出：5
#   解释：
#   intention -> inention (删除 't')
#   inention -> enention (将 'i' 替换为 'e')
#   enention -> exention (将 'n' 替换为 'x')
#   exention -> exection (将 'n' 替换为 'c')
#   exection -> execution (插入 'u')
#######################################################################################

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype int

        (knowledge)

        思路：
            其实总共有四种操作，插入、删除、替换和什么都不操作
        1. 使用动态规划；
        2. 定义状态：dp[i][j] => word1前i个字符构成的子串与word2前j个字符构成的子串的编辑距离；
        3. base case => dp[i][0] = i, dp[0][j] = j => 表示其中一个子串为空的情形
        4. 状态转移方程：
            f(i, j) =   0                             i == 0 || j == 0
                        f(i - 1, j - 1)               i > 0 && j > 0 && word1[i] == word2[j]
                        min {                         i > 0 && j > 0 && word1[i] != word2[j]  
                            f(i - 1, j) + 1,
                            f(i, j - 1) + 1,
                            f(i - 1, j - 1) + 1
                        }

        tip: 可以参考 => https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/bian-ji-ju-li
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for i in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][0] = i

        for j in range(1, n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,
                        dp[i][j - 1] + 1,
                        dp[i - 1][j - 1] + 1
                    )

        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minDistance("horse", "ros"), "= 3")
    print(solution.minDistance("intention", "execution"), "= 5")
