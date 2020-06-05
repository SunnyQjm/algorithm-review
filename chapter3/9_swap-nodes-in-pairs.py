#!/usr/bin/env python
# coding=utf-8

###############################################################################
# Leetcode 24 两两交换链表中的节点
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
###############################################################################

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        if self:
            return "{}->{}".format(self.val, repr(self.next))


class Solution:
    def swapPairs(self, head):
        """
        
        (knowledge)

        思路：
        1. 用三个指针pre(初始为None)，cur(初始为head)，next(初始位head.next)；
        2. 接着借由三个指针完成两个节点的交换
        """
        if head is None or head.next is None:
            return head
        pre, cur, next, head = None, head, head.next, head.next
        while cur is not None and next is not None:
            if pre is not None:
                pre.next = cur.next
            cur.next, next.next, cur, pre = next.next, cur, next.next, cur
            if cur is not None:
                next = cur.next
        return head


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(solution.swapPairs(head))
