#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 787 K 站中转内最便宜的航班
# 
# 题目太长了，瞅这 => https://leetcode-cn.com/problems/cheapest-flights-within-k-stops/
#######################################################################################

from typing import List
import collections, heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        """
        :type n: int 城市个数
        :type flights: List[List[int]]  m个航班
        :type src: int 出发城市
        :type dst: int 到达城市
        :type K: int 最大中转次数
        :rtype int

        (knowledge)

        思路：
        1. 执行Djikstra算法计算最短距离的算法，过程中传递当前的跳数，当跳数超过k+1时进行剪枝；
        2. 使用最小堆来简化Djikstra代码实现； 
        3. 过程中一旦遍历到目的节点，就返回;
        """

        # 这边使用字典来统一表示图
        graph = collections.defaultdict(dict)

        # 构建图
        for u, v, w in flights:
            graph[u][v] = w

        # 最小堆中的每个元素为一个三元组，<源节点到当前节点的开销，源节点到当前节点走了几跳，当前节点编号>
        pq = [(0, 0, src)]

        while pq:

            # 从最小堆中取出cost最小的元素
            cost, step, place = heapq.heappop(pq)

            # 如果到达当前节点的跳数大于K+1，则跳过
            if step > K + 1:
                continue

            if place == dst:
                return cost

            # 遍历当前节点的所有邻居
            for neighbour, weight in graph[place].items():
                heapq.heappush(pq, (cost + weight, step + 1, neighbour))
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1), "= 200")
    print(solution.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0), "= 500")
