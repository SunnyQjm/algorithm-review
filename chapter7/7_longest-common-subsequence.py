#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# leecode 1143 最长公共子序列
#
# 给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。
# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。
# 若这两个字符串没有公共子序列，则返回0。
#
# 示例 1:
#   输入：text1 = "abcde", text2 = "ace" 
#   输出：3  
#   解释：最长公共子序列是 "ace"，它的长度为 3。
#
# 示例 2:
#   输入：text1 = "abc", text2 = "abc"
#   输出：3
#   解释：最长公共子序列是 "abc"，它的长度为 3。
#
# 示例 3:
#   输入：text1 = "abc", text2 = "def"
#   输出：0
#   解释：两个字符串没有公共子序列，返回 0。
#######################################################################################

class Solution:
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1:str
        :type text2:str
        :rtype int

        (knowledge)

        思路：
        1. 使用动态规划；
        2. 定义状态：dp[i][j] => 表示text1的前i个字符构成的子串和text2的前j个字符构成的子串的最长公共子序列长度；
        3. base case => dp[0][...]和dp[...][0]都应该为0，表示其中一个串为空串的情况下，最长公共子序列长度自然为0；
        4. 状态转移方程如下：
            f(i, j) = 0                                         i == 0 || j == 0
                      f(i - 1, j - 1) + 1                       i > 0 && j > 0 && text1[i] == text2[j]
                      max{f(i - 1, j), f(i, j - 1)}             i > 0 && j > 0 && text1[i] != text2[j]

        tip: 可以参考这边的分析 => https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/zui-chang-gong-gong-zi-xu-lie
        """
        m, n = len(text1), len(text2)
        # 初始化dp数组
        dp = [[0] * (n + 1) for i in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonSubsequence("abcde", "ace"), "\n= 3")
    print(solution.longestCommonSubsequence("abc", "abc"), "\n= 3")
    print(solution.longestCommonSubsequence("abc", "def"), "\n= 0")

