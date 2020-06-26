#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 239 滑动窗口最大值
#
# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
# 返回滑动窗口中的最大值。
#
# 进阶：
#   你能在线性时间复杂度内解决此题吗？
#
# 示例:
#   输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
#   输出: [3,3,5,5,6,7] 
#   解释: 
#
#     滑动窗口的位置                最大值
#   ---------------               -----
#   [1  3  -1] -3  5  3  6  7       3
#    1 [3  -1  -3] 5  3  6  7       3
#    1  3 [-1  -3  5] 3  6  7       5
#    1  3  -1 [-3  5  3] 6  7       5
#    1  3  -1  -3 [5  3  6] 7       6
#    1  3  -1  -3  5 [3  6  7]      7
#
# 提示：
#   1 <= nums.length <= 10^5
#   -10^4 <= nums[i] <= 10^4
#   1 <= k <= nums.length
#######################################################################################

import collections


class Solution:
    def maxSlidingWindow(self, nums, k):
        """

        (knowledge)

        思路：
        1. 用一个队列记录当前处于窗口内的值，这个队列有如下性质：
            - 队列中的元素不会超过窗口大小k；
            - 保证队头的元素总是队列里面最大的；
        2. 每次有数据入队时都执行如下流程：
            - 判断当前队列长度是否为k，如果是则首先pop一个元素，并依次比对，进行若干次出队，把当前队列的最大值排到队首；
            - 然后将队首元素与预入队元素比对，如果小于等于将要入队的元素，则出队；
            - 循环执行上一步骤，直到队列为空或者队首元素大于将要入队的元素；
            - 最后将要入队的元素入队。
        3. 初始时，先用步骤2的方法，入队k-1个元素，从第k个元素开始，每次入队完，队首的元素即为当前窗口的最大值。


        PS: 关于上述算法的流程，这边有一个leetcode官方制作的动画演示：
            https://leetcode-cn.com/problems/sliding-window-maximum/solution/shi-pin-jie-xi-shuang-duan-dui-lie-hua-dong-chuang/
        """

        def easyEnqueue(queue, num, k):

            # 当前队列中的元素数量和窗口大小一致，此时要入队需要额外处理（保证队列中的元素个数小于等于窗口数量）
            if len(queue) == k:
                # 此时要入队，肯定要先出队一个元素，将最左边的元素出队
                queue.popleft()

                # maxValue 记录本次调整后窗口内的最大值，初始置为将要入队的元素
                # maxValue 记录本次调整后窗口内的最大值元素在队列中的下标，初始置为队列的大小（表示将要入队的元素的位置）
                maxValue, maxIndex = num, len(queue)

                # 通过一轮循环，找到最大值和最大值的索引
                for index, v in enumerate(queue):
                    if v > maxValue:
                        maxValue = v
                        maxIndex = index

                # 将最大值以左的所有元素出队（当前窗口最大值以左的元素已经用不到了，没有必要保留）
                for index in range(maxIndex):
                    queue.popleft()

            # 如果当前队列不为空，依次判断队列中的元素是否小于等于将要入队的元素，如果是则出队
            while queue:
                if queue[0] <= num:
                    queue.popleft()
                else:
                    break

            # 将要入队的元素入队
            queue.append(num)

        # 特判，当数组小于等于窗口大小时，不需要滑动，直接返回数组的最大值即可
        if len(nums) <= k:
            return [max(nums)]

        # queue用来存储当前窗口的元素（不一定是全部元素，窗口内最大值以左的元素都出队了）
        # res用来存储最终的结果（每个窗口的最大值）
        queue, res = collections.deque(), []

        # 先将前k-1个元素入队
        for i in range(k - 1):
            easyEnqueue(queue, nums[i], k)

        # 从第k个元素开始，每入队一个元素，都得到一个当前窗口的最大值（队头元素）
        for i in range(k - 1, len(nums)):
            easyEnqueue(queue, nums[i], k)
            res.append(queue[0])

        return res

    def maxSlidingWindow2(self, nums, k):
        if not nums:
            return []
        # window是一个双向队列
        # res记录结果
        window, res = [], []

        for i, x in enumerate(nums):
            # 如果当前window中的元素已经有k个了，首先pop掉一个最先入队的元素
            if i >= k and window[0] <= i - k:
                window.pop(0)

            # 将比待插入值小的都右出队
            while window and nums[window[-1]] <= x:
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3), "= \n[3, 3, 5, 5, 6, 7]")
    print(solution.maxSlidingWindow([1, 3, 1, 2, 0, 5], 3), "= \n[3, 3, 2, 5]")
    print(solution.maxSlidingWindow([9, 10, 9, -7, -4, -8, 2, -6], 5), "= \n[10, 10, 9, 2]")

    print(solution.maxSlidingWindow2([1, 3, -1, -3, 5, 3, 6, 7], 3), "= \n[3, 3, 5, 5, 6, 7]")
    print(solution.maxSlidingWindow2([1, 3, 1, 2, 0, 5], 3), "= \n[3, 3, 2, 5]")
    print(solution.maxSlidingWindow2([9, 10, 9, -7, -4, -8, 2, -6], 5), "= \n[10, 10, 9, 2]")
