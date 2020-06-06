#!/usr/bin/env python
# coding=utf-8

##########################################################################
# Leetcode 58 最后一个单词的长度
#
# 给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。
# 如果不存在最后一个单词，请返回 0 。
# 
# 说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。
#
# 示例:
#   输入: "Hello World"
#   输出: 5
##########################################################################

class Solution: 
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype int

        (knowledge)

        思路：
        1. 先将字符串两端的空格去除；
        2. 然后，从后往前遍历，遇到一个非空格，计数+1，遇到一个空格就停止计数；
        3. 返回计数结果
        """

        # 首先去除字符串两边的空格
        s, result = s.strip(), 0

        # 反向遍历字符串，统计最后一个单词的长度，遇到第一个空格跳出
        for i in range(len(s))[::-1]:
            if s[i] == ' ':
                break
            else:
                result += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLastWord("Hello World"), "= 5")
