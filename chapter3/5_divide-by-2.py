#!/usr/bin/env python
# coding=utf-8


##########################################################
# 栈的应用——十进制转二进制
##########################################################

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

class Solution:
    def divideBy2(self, decNumber):
        """
        
        (knowledge)

        算法功能说明：传入一个正整数，将其转换为2进制表达方式

        思路：
        1. 依次除2取余，使用栈保存余数
        2. 接着依次弹栈，构造出二进制串
        """
        stack = Stack()

        while decNumber > 0:
            stack.push(decNumber % 2)
            decNumber = decNumber // 2

        result = ""
        while not stack.isEmpty():
            result += str(stack.pop())
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.divideBy2(233), "= 11101001")
    print(solution.divideBy2(42), "= 101010")
