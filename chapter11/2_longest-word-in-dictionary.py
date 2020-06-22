#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 720 词典中最长的单词
#
# 给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成。若其中有多个可行的答案，则返回答案中字典序最小的单词。
# 若无答案，则返回空字符串。
#
# 示例 1:
#   输入: 
#   words = ["w","wo","wor","worl", "world"]
#   输出: "world"
#   解释: 
#   单词"world"可由"w", "wo", "wor", 和 "worl"添加一个字母组成。
#
# 示例 2:
#   输入: 
#   words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
#   输出: "apple"
#   解释: 
#   "apply"和"apple"都能由词典中的单词组成。但是"apple"得字典序小于"apply"。
#
# 注意:
#   - 所有输入的字符串都只包含小写字母。
#   - words数组长度范围为[1,1000]。
#   - words[i]的长度范围为[1,30]。
#######################################################################################

from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        """
        :type words: List[str]
        :rtype str
        
        (knowledge)

        思路：  
        1. 用一个集合valid存储满足题目中限定的若干字符串；
        2. 根据长度对原字符串列表排序，然后对排序后的字符串列表进行遍历；
        3. 对每个字符串word，判断word[:-1]是否在valid当中，在则将其也放入到valid当中
        4. 最后对valid进行按字典序排序，然后返回长度最大的元素即可
        """

        valid = set([""])

        for word in sorted(words, key=len):
            if word[:-1] in valid:
                valid.add(word)

        return max(sorted(valid), key=len)


if __name__ == '__main__':
    solution = Solution()
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    print(solution.longestWord(words), "= apple")
