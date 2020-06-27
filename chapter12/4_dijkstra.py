#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Dijkstra 单源最短路径算法
#######################################################################################

from typing import Dict
import heapq


def dijkstra(distances: Dict, origin: str) -> Dict:
    """
    :type distances: Dict[Dict]         表示所有的带权边
    :type origin: str                   起点
    :rtype Dict
    """

    # visited => 记录节点源节点到它的最短路径（已经在visited里面的点都是已确定最短路径的点）
    # pq => 一个最小堆，用来存放候选节点
    visited, pq = {}, [(0, origin)]

    while pq:
        distance, node = heapq.heappop(pq)

        # 跳过已遍历的节点
        if node in visited:
            continue

        # 将当前节点放入已确定最短距离的集合中
        visited[node] = distance

        # 遍历当前节点所有的邻居，如果该邻居不在visited里面，则将通过当前节点到达该邻居的距离以及邻居的名字放入堆中
        for neighbour, cost in distances[node].items():
            if neighbour not in visited:
                heapq.heappush(pq, (distance + cost, neighbour))
    return visited


if __name__ == '__main__':
    distances = {
        'S': {'A': 6, 'B': 2},
        'A': {'E': 1},
        'B': {'A': 3, 'E': 5},
        'E': {'E': 0}
    }
    print(dijkstra(distances, 'S'))
