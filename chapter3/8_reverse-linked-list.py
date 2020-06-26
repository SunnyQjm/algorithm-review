#!/usr/bin/env python
# coding=utf-8

###########################################################################
# Leetcode 206 反转链表
#
# 反转一个单链表。
#
# 示例:
#   输入: 1->2->3->4->5->NULL
#   输出: 5->4->3->2->1->NULL
#
# 进阶:
#   你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
###########################################################################


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{}->{}".format(self.val, repr(self.next))


class Solution:
    def reverseList(self, head):
        """

        (knowledge)

        思路：
        1. 用两个指针，一个指针指向新链（初始为None），一个指向原链（初始为head）；
        2. 从头往后依次遍历，进行反挂；
        
        tip:跟着代码执行的流程，画个图，很快就能get到代码的实现思路了
        """
        cur = None
        while head is not None:
            head.next, cur, head = cur, head, head.next
        return cur


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    solution = Solution()
    print(solution.reverseList(head))
