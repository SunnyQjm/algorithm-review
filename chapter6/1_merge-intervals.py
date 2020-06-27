#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 56 合并区间
#   https://leetcode-cn.com/problems/merge-intervals/
#
# 给出一个区间的集合，请合并所有重叠的区间。
#
# 示例 1:
#   输入: [[1,3],[2,6],[8,10],[15,18]]
#   输出: [[1,6],[8,10],[15,18]]
#   解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
# 示例 2:
#   输入: [[1,4],[4,5]]
#   输出: [[1,5]]
#   解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
#######################################################################################

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype List[List[int]]

        (Knowledge)

        思路：
        1. 首先对输入的区间数组进行排序；
        2. 接着用两个指针，cur指向当前处理的区间，next指向下一个要处理的区间；
        3. 根据cur和next所指区间的情况，分别处理：
            - intervals[cur] 和 intervals[next]区间没有重叠，则令intervals[cur + 1] = intervals[next], cur++, next++
            - intervals[cur][1] >= intervals[next][0]，则令intervals[cur][1] = max(intervals[cur][1], intervals[next][1]), next++
        4. 最后返回intervals[:cur + 1]
        """

        # 首先对输入的区间数组进行排序
        intervals = sorted(intervals)
        cur, next = 0, 1

        while next < len(intervals):
            if intervals[next][0] > intervals[cur][1]:  # 处理没有重叠的情况
                intervals[cur + 1], cur, next = intervals[next], cur + 1, next + 1
            else:  # 处理有重叠的情况
                intervals[cur][1], next = max(intervals[cur][1], intervals[next][1]), next + 1

        return intervals[:cur + 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]), "= [[1, 6], [8, 10], [15, 18]]")
    print(solution.merge([[1, 4], [4, 5]]), "= [[1, 5]]")
