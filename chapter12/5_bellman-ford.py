#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Bellman-Ford 单源最短路径算法
#######################################################################################
from typing import Dict


def bellmanFord(distances: Dict, origin: str):
    # edges => 用来存放所有的边
    # result => 用来存放最短距离的映射结果
    edges, result = [], {}
    for node, neighbours in distances.items():
        for neighbour, weight in neighbours.items():
            edges.append((node, neighbour, weight))
        result[node] = float('inf')
    result[origin] = 0

    # 每轮都使用所有的边对节点进行松弛操作，最多运行n-1轮
    for i in range(len(distances) - 1):
        for u, v, w in edges:
            if result[v] > result[u] + w:
                result[v] = result[u] + w
    return result


if __name__ == '__main__':
    distances = {
        'A': {'C': 4, 'B': 2},
        'B': {'A': 1, 'G': 1},
        'C': {'B': -3, 'G': 1},
        'G': {}
    }
    print(bellmanFord(distances, 'A'))
