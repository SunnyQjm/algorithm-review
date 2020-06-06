#!/usr/bin/env python
# coding=utf-8

###################################################################################
# Leetcode 19 删除链表的倒数第N个节点
#
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#   给定一个链表: 1->2->3->4->5, 和 n = 2.
#   当删除了倒数第二个节点后，链表变为 1->2->3->5.
#
# 说明：
#   给定的 n 保证是有效的。
#
# 进阶：
#   你能尝试使用一趟扫描实现吗？
###################################################################################

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        if self:
            return "{}->{}".format(self.val, repr(self.next))

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype ListNode

        (knowledge)

        思路：
        1. 用双指针法；
        2. 首先让一个right指针，先指向第n + 1个节点，让一个left指针指向头节点；
        3. 然后让两个指针一起右移，直到right指针为None停止；（过程中使用pre指针记录left指针的左边节点，初始pre为None）
        4. 最后删除left指向的那个节点即可
        """
        pre, left, right = None, head, head

        # 首先让right指针指向第n + 1个节点
        for i in range(n):
            right = right.next

        # left和right两个指针一起右移，同时使用pre记录left指针的左边节点
        while right:
            pre, left, right = left, left.next, right.next

        if not pre: # 处理要删除的节点是头节点的情况
            return head.next
        else:
            pre.next = left.next
            return head


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(solution.removeNthFromEnd(head, 2), "= 1->2->3->5")
