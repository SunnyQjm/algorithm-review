#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 847 访问所有节点的最短路径
# 
# 给出 graph 为有 N 个节点（编号为 0, 1, 2, ..., N-1）的无向连通图。 
# graph.length = N，且只有节点 i 和 j 连通时，j != i 在列表 graph[i] 中恰好出现一次。
# 返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。
#
# 示例 1：
#   输入：[[1,2,3],[0],[0],[0]]
#   输出：4
#   解释：一个可能的路径为 [1,0,2,0,3]
#
# 示例 2：
#   输入：[[1],[0,2,4],[1,3,4],[2],[1,2]]
#   输出：4
#   解释：一个可能的路径为 [0,1,4,2,3]
#
# 提示：
#   1. 1 <= graph.length <= 12
#   2. 0 <= graph[i].length < graph.length
#######################################################################################

import collections
from typing import List

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        """
        :type graph: List[List[int]]
        :rtype int

        (knowledge)

        思路：
        1. 首先引入一个用位压缩来表示当前图中节点访问状态的一个概念，何谓位压缩？
            题中提到，图的节点个数不会超过十二个，那我们完全可以用一个数字的前N位来标记图中哪些节点已经被访问，而哪些没有：
            例如：0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 => 即 表示编号为1和3的节点已经访问过了，其它节点还没有被访问

        2. 然后我们定一个遍历过程中的状态元组，(位压缩表示，节点编号) => 表示当前处于某个节点上，且位压缩对应的是当前哪些节点已经遍历过了
            例如：(7, 0) => 表示当前处于编号为0的节点，并且编号为0、1、2的节点已经访问过了
                7 => 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1

        3. 根据上面的讨论，我们结束的目标 END 就是得到一个位压缩表示，其值为 (1 << N) - 1
            例如：N = 8
                (1 << N) => 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 
            (1 << N) - 1 => 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1

        4. 我们初始时以每一个节点为起点，同时向外泛洪扩张，直到某一时刻得到结束状态 END
        """
        # 得到图节点个数
        N = len(graph)

        # 结束标记
        END = (1 << N) - 1
        
        # 初始以图中所有节点为出发点
        queue = [(1 << i, i) for i in range(N)]

        # 用一个字典记录当前图要达到某一个状态，所需的最短路径长度
        dist = collections.defaultdict(lambda: N * N)

        # 达到某一个节点访问了，其它节点没有访问的状态，只要以该节点为起点就可，所以距离为0
        for i in range(N):
            dist[(1 << i, i)] = 0

        while queue:

            # 取出队头元素
            cover, node = queue.pop(0)

            # 获取要达到该状态目前记录的最短距离，默认为N*N
            d = dist[(cover, node)]

            # 如果当前状态是目标状态，则直接返回其对应距离
            if cover == END:
                return d

            # 遍历其所有邻居
            for child in graph[node]:
                newCover = cover | (1 << child)

                # 如果通过该邻居到达一个新的状态所需的总得距离小于之前记录的距离，则加入到队列当中
                if d + 1 < dist[(newCover, child)]:
                    dist[(newCover, child)] = d + 1
                    queue.append((newCover, child))


if __name__ == '__main__':
    solution = Solution()
    print(solution.shortestPathLength([[1,2,3],[0],[0],[0]]), "= 4")
    print(solution.shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]]), "= 4")