#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 703 数据流中的第K大元素
#
# 设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。
# 你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，它包含数据流中的初始元素。每次调用 KthLargest.add，返回当前数据流中第K大的元素。
#
# 示例:
#   int k = 3;
#   int[] arr = [4,5,8,2];
#   KthLargest kthLargest = new KthLargest(3, arr);
#   kthLargest.add(3);   // returns 4
#   kthLargest.add(5);   // returns 5
#   kthLargest.add(10);  // returns 5
#   kthLargest.add(9);   // returns 8
#   kthLargest.add(4);   // returns 8
#
# 说明:
#   你可以假设 nums 的长度≥ k-1 且k ≥ 1。
#######################################################################################

import heapq


class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heap = nums
        heapq.heapify(self.heap)  # 用一个列表作为堆（使用heapq对其操作）
        self.currentSize = len(nums)  # 保存当前堆中元素的个数
        self.k = k
        while self.currentSize > k:
            heapq.heappop(self.heap)
            self.currentSize -= 1

    def add(self, val):
        """
        :type val: int
        :rtype: int

        (knowledge)

        思路：
        1. 这是堆的应用，每次要返回第K大的元素，则表示我们只要维持当前最大的到第K大的元素即可，更小的可以忽略；
        2. 对初始传入的nums进行堆构造，并删除堆顶元素直至堆中元素个数小于等于k时停止；
        3. 每次插入时执行以下流程：
            - 首先判断当前堆的大小是k还是k-1；（因为题目中指出，nums >= k-1，所以初始堆中元素个数至少为k-1，又因为我们在初始化时进行了堆删除，删到小于等于k为止，所以堆中元素最多有k个）
            - 如果currentSize == k-1，则插入当前元素到堆中，并返回堆顶元素即可；
            - 如果currentSize > k-1, 则将当前元素插入到堆中，接着再删除堆顶元素，并返回堆顶元素；（这样可以保证堆中元素一直是k个）
        """
        if self.currentSize == self.k - 1:
            heapq.heappush(self.heap, val)
            self.currentSize += 1
        else:
            heapq.heappush(self.heap, val)
            heapq.heappop(self.heap)

        return self.heap[0]


if __name__ == '__main__':
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    print(kthLargest.add(3), "= 4")
    print(kthLargest.add(5), "= 5")
    print(kthLargest.add(10), "= 5")
    print(kthLargest.add(9), "= 8")
    print(kthLargest.add(4), "= 8")
