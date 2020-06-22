#!/usr/bin/env python
# coding=utf-8

#######################################################################################
# Leetcode 997 找到小镇的法官
#
# 在一个小镇里，按从 1 到 N 标记了 N 个人。传言称，这些人中有一个是小镇上的秘密法官。
# 如果小镇的法官真的存在，那么：
#   1. 小镇的法官不相信任何人。
#   2. 每个人（除了小镇法官外）都信任小镇的法官。
#   3. 只有一个人同时满足属性 1 和属性 2 。
# 给定数组 trust，该数组由信任对 trust[i] = [a, b] 组成，表示标记为 a 的人信任标记为 b 的人。
# 如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的标记。否则，返回 -1。
#
# 示例 1：
#   输入：N = 2, trust = [[1,2]]
#   输出：2
#
# 示例 2：
#   输入：N = 3, trust = [[1,3],[2,3]]
#   输出：3
#
# 示例 3：
#   输入：N = 3, trust = [[1,3],[2,3],[3,1]]
#   输出：-1
#
# 示例 4：
#   输入：N = 3, trust = [[1,2],[2,3]]
#   输出：-1
#
# 示例 5：
#   输入：N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
#   输出：3
#
# 提示：
#   1. 1 <= N <= 1000
#   2. trust.length <= 10000
#   3. trust[i] 是完全不同的
#   4. trust[i][0] != trust[i][1]
#   5. 1 <= trust[i][0], trust[i][1] <= N
#######################################################################################

from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype int

        (knowledge)

        思路：
        1. 将整个信任关系构建成一个图，a信任b表示a到b之间有条a->b的有向边；
        2. 很容易直到，符合条件的法官要求入度为N-1，出度为0；
        3. 所以只要找到入度为N-1的点，并判断其出度是否为0即可。
        """
        # 特判只有一个人的情况，不构成图
        if N == 1:
            return 1

        # 用两个字典分别记录入度和出度
        inDegree, outDegree = {}, {}

        # 遍历所有的边，记录所有的出度入度
        for trust_element in trust:
            if trust_element[0] in outDegree:
                outDegree[trust_element[0]] += 1
            else:
                outDegree[trust_element[0]] = 1
            if trust_element[1] in inDegree:
                inDegree[trust_element[1]] += 1
            else:
                inDegree[trust_element[1]] = 1

        # 遍历入度记录表，找到入度为N-1的人，并判断其出度是否为0
        for key, value in inDegree.items():
            if value == N - 1 and key not in outDegree:
                return key

        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.findJudge(2, [[1, 2]]), "= 2")
    print(solution.findJudge(3, [[1, 3], [2, 3]]), "= 3")
    print(solution.findJudge(3, [[1, 3], [2, 3], [3, 1]]), "= -1")
    print(solution.findJudge(3, [[1, 2], [2, 3]]), "= -1")
    print(solution.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]), "= 3")
