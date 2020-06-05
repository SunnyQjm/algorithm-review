#!/usr/bin/env python
# coding=utf-8

###########################################################################
# Leetcode 20 有效的括号
# 
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 有效字符串需满足：
#   1. 左括号必须用相同类型的右括号闭合。
#   2. 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#   输入: "()"
#   输出: true
#
# 示例 2:
#   输入: "()[]{}"
#   输出: true
#
# 示例 3:
#   输入: "(]"
#   输出: false
#
# 示例 4:
#   输入: "([)]"
#   输出: false
#
# 示例 5:
#   输入: "{[]}"
#   输出: true
###########################################################################

class Solution:
    def isValid(self, s):
        """

        (knowledge)

        思路：
        1. 用栈，遇到左括号就推入栈；
        2. 遇到右括号就比对栈顶的括号和其是否匹配；
            - 不匹配则返回False
            - 匹配则将栈顶弹出
            - 如果此时栈为空，则返回False
        3. 循环2直至遍历完成，最后，如果栈不为空则返回False，否则返回True

        """
        # 这边用list来模拟栈
        stack = []

        # 一个字典，用来记录括号映射
        dict = {'(': ')', '{': '}', '[': ']'}

        for c in s:
            if c in dict:
                stack.append(c)
            elif len(stack) == 0 or dict[stack.pop()] != c:
                return False
        return len(stack) == 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid("()"), "= True")
    print(solution.isValid("()[]{}"), "= True")
    print(solution.isValid("(]"), "= False")
    print(solution.isValid("([)]"), "= False")
    print(solution.isValid("{()}"), "= True")

