#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 5 最长回文子串
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#   输入: "babad"
#   输出: "bab"
#   注意: "aba" 也是一个有效答案。
#
# 示例 2：
#   输入: "cbbd"
#   输出: "bb"
#######################################################################################


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype str

        (knowledge)

        思路：
        1. 使用动态规划
        2. dp[i][j] => s[i:j] 子串是否是一个回文字符串
        3. 状态转移方程
           f(i, j) = True                               i == j
                     s[i] == s[j]                       i + 1 == j
                     f(i + 1, j - 1) && s[i] == s[j]    i + 1 < j
        """
        dp, resultStart, resultEnd = [[True if i == j else False for j in range(len(s))] for i in range(len(s))], 0, 1

        for j in range(0, len(s) - 1):
            dp[j][j + 1] = s[j] == s[j + 1]
            if dp[j][j + 1]:
                resultStart, resultEnd = j, j + 2

        for i in range(2, len(s)):
            for j in range(0, len(s) - i):
                if dp[j + 1][j + i - 1] and s[j] == s[j + i]:
                    resultStart, resultEnd, dp[j][j + i] = j, j + i + 1, True
        return s[resultStart: resultEnd]


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome("abcba"), "= abcba")
    print(solution.longestPalindrome("babad"), "= aba")
    print(solution.longestPalindrome("cbbd"), "= bb")
    print(solution.longestPalindrome("ccc"), "= ccc")
