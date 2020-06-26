#!/usr/bin/env python
# coding=utf-8

################################################################################
# Leetcode 83 删除排序链表中的重复元素
#
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
#
# 示例 1:
#   输入: 1->1->2
#   输出: 1->2
#
# 示例 2:
#   输入: 1->1->2->3->3
#   输出: 1->2->3
################################################################################


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        if self:
            return "{}->{}".format(self.val, repr(self.next))


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtypr ListNode

        (Knowledge)

        1. 用两个指针，pre指向当前遍历节点的前一个节点，cur指向当前节点；
        2. 每次查看当前值和上一次访问的数字是否相同，相同则执行删除节点操作，不相同则两个指针右移
        """
        if not head:
            return None
        pre, cur = head, head.next

        while cur:
            if cur.val == pre.val:
                pre.next = cur.next
            else:
                last, pre = cur.val, cur
            cur = cur.next

        return head


if __name__ == '__main__':
    solution = Solution()
    h1 = ListNode(1)
    h1.next = ListNode(1)
    h1.next.next = ListNode(2)
    print(solution.deleteDuplicates(h1), "= 1->2")
    
    h1 = ListNode(1)
    h1.next = ListNode(1)
    h1.next.next = ListNode(2)
    h1.next.next.next = ListNode(3)
    h1.next.next.next.next = ListNode(3)
    print(solution.deleteDuplicates(h1), "= 1->2->3")
