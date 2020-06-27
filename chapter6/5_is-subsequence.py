#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 392  判断子序列
#
# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
# 你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
#
# 示例 1:
#   s = "abc", t = "ahbgdc"
#   返回 true.
#
# 示例 2:
#   s = "axc", t = "ahbgdc"
#   返回 false. 
#
# 后续挑战 :
#   如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？
#
#######################################################################################


class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype bool

        (knowledge)

        思路：
        1. 直接用两个指针，sPtr指向短串s，tPtr指向长串t；
        2. 依次按需在长串中找到子串中的每一个字符，都找到返回true，否则返回false
        """
        if len(s) > len(t):
            return False

        sPtr, tPtr, lenS, lenT = 0, 0, len(s), len(t)
        while sPtr < lenS and tPtr < lenT:
            if s[sPtr] == t[tPtr]:
                sPtr += 1
            tPtr += 1
        return sPtr == len(s)


if __name__ == '__main__':
    solution = Solution()
    print(solution.isSubsequence("abc", "ahbgdc"), "= True")
    print(solution.isSubsequence("acb", "ahbgdc"), "= False")
    print(solution.isSubsequence("axc", "ahbgdc"), "= False")
