#!/usr/bin/env python
# coding=utf-8

############################################################
# 双向队列的应用——回文检查
############################################################

import collections

class Solution:
    def palchecker(self, str):
        """
        算法功能说明：输入一个字符串，返回一个bool值表示该字符串是否是回文

        思路：
        1. 使用一个双向队列，首先将字符串中的每个字符入队；
        2. 接着比对队头和队尾两个字符是否相等，相等则头尾同时出队（如果只剩一个元素，出队一次即可），不相等则返回False

        PS: 关于collections的使用 => https://www.liaoxuefeng.com/wiki/1016959663602400/1017681679479008
        """
        # 使用python内置的双向队列实现
        dqueue = collections.deque()

        # 将所有字符入队
        for c in str:
            dqueue.append(c)
        
        # 依次判断首尾字符是否相同
        while len(dqueue) > 1:
            if dqueue.pop() != dqueue.popleft():
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.palchecker("abbba"), "= True")
    print(solution.palchecker("qwertgtrewq"), "= True")
    print(solution.palchecker("a"), "= True")
    print(solution.palchecker("abcbc"), "= False")

