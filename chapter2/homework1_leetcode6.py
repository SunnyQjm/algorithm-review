#!/usr/bin/env python
# coding=utf-8

############################################################
# Z 字形变换
# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
#   L   C   I   R
#   E T O E S I I G
#   E   D   H   N
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
# 请你实现这个将字符串进行指定行数变换的函数：
#   string convert(string s, int numRows);
#
# 示例 1：
#   输入: s = "LEETCODEISHIRING", numRows = 3
#   输出: "LCIRETOESIIGEDHN"
#
# 示例 2:
#   输入: s = "LEETCODEISHIRING", numRows = 4
#   输出: "LDREOEIIECIHNTSG"
#   解释:
#
#   L     D     R
#   E   O E   I I
#   E C   I H   N
#   T     S     G
############################################################

import collections


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
       :rtype: str

       (Knowledge)

        算法思路: 
        
         1. 用numRows个list记录每行的字符串；

         2. 然后顺序遍历字符串，按Z字形顺序放到合适的行中；

         3. 最后将每行的字符串拼接即可
        """
        if numRows == 1:
            return s

        lines = [[] for i in range(numRows)]

        # 当前的方向（首先向下，触底向上，触顶向下，依次改变方向）
        goDown = True

        # 下一个字符要写入的行号，初始为0,根据方向进行更新，向下则+1,向上则-1
        lineNumber = 0

        # 依次遍历字符串，按Z字型顺序写到合适的行
        for i in range(len(s)):
            lines[lineNumber].append(s[i])

            # 判断是否需要改变方向
            if goDown and lineNumber == numRows - 1:
                goDown = False
            if not goDown and lineNumber == 0:
                goDown = True

            # 根据当前的方向更新行号
            lineNumber = lineNumber + 1 if goDown else lineNumber - 1

        # 将所有numRows个list拼接成一个list
        for i in range(1, numRows):
            lines[0] += lines[i]

        # 将list转字符串返回
        return "".join(lines[0])


if __name__ == '__main__':
    solution = Solution()
    print(solution.convert("LEETCODEISHIRING", 3), "= \nLCIRETOESIIGEDHN")
    print(solution.convert("LEETCODEISHIRING", 4), "= \nLDREOEIIECIHNTSG")
