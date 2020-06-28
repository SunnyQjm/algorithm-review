#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 148  排序链表
#
# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
#
# 示例 1:
#   输入: 4->2->1->3
#   输出: 1->2->3->4
#
# 示例 2:
#   输入: -1->5->3->4->0
#   输出: -1->0->3->4->5
#######################################################################################


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{}->{}".format(self.val, repr(self.next))


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype ListNode

        (knowledge)

        思路：
        1. 使用递归方式实现链表的归并排序算法；
        2. 对链表进行分治的时候，可以使用快慢指针（快指针一次走两步，慢指针一次走一步，同时从head出发，当快指针走到链表尾的时候，慢指针就走到中间位置）；
        """

        # 链表为空或者只有一个元素，直接返回
        if not head or not head.next:
            return head

        # low -> 右子链的头部
        # pre -> 左子链最后一个节点（未断开之前，指向low）
        low, fast, pre = head, head, None
        while fast and fast.next:
            low, fast, pre = low.next, fast.next.next, low

        # 断开左右子链之间的链接
        pre.next = None

        # 对左右子链分别递归的进行归并排序
        head = self.sortList(head)
        low = self.sortList(low)

        # 对排好序的两部分进行归并
        if not low:
            return head

        result, cur = self, None
        while head and low:
            if head.val <= low.val:
                result.next, head = head, head.next
            else:
                result.next, low = low, low.next
            result = result.next

        if not head:
            result.next = low
        elif not low:
            result.next = head
        else:
            result.next = None
        return self.next


if __name__ == '__main__':
    solution = Solution()
    h1 = ListNode(4)
    h1.next = ListNode(2)
    h1.next.next = ListNode(1)
    h1.next.next.next = ListNode(3)
    print(solution.sortList(h1), "= 1->2->3->4")
