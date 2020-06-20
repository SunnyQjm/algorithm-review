#!/usr/bin/env python
# coding=utf-8


#######################################################################
# 队列的应用——烫手山芋问题（约瑟夫问题）
#
# 据说著名犹太历史学家 Josephus有过以下的故事：在罗马人占领乔塔帕特后，39 个犹太人与Josephus及他的朋友躲到一个洞中，
# 39个犹太人决定宁愿死也不要被敌人抓到，于是决定了一个自杀方式，41个人排成一个圆圈，由第1个人开始报数，每报数到第3人该人就必须自杀，
# 然后再由下一个重新报数，直到所有人都自杀身亡为止。然而Josephus 和他的朋友并不想遵从。首先从一个人开始，越过k-2个人（因为第一个人已经被越过），
# 并杀掉第k个人。接着，再越过k-1个人，并杀掉第k个人。这个过程沿着圆圈一直进行，直到最终只剩下一个人留下，这个人就可以继续活着。
# 问题是，给定了和，一开始要站在什么地方才能避免被处决？Josephus要他的朋友先假装遵从，他将朋友与自己安排在第16个与第31个位置，于是逃过了这场死亡游戏。
#######################################################################

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Solution:
    def hotPotato(self, nameList, num):
        """
        
        (knowledge)

        算法功能描述：堆名称列表里的人，每数num个人枪毙一个第num个人

        思路：
        1. 首先将所有人入队；
        2. 然后将前num - 1个人出队，入队，则第num个人处于队头位置，直接出队不入队；（这边说的前num - 1个人不一定都是不同的人，人少的时候可能绕一圈轮到同一个人）
        3. 重复2，直至队列为空
        """
        queue = Queue()
        for name in nameList:
            queue.enqueue(name)

        while not queue.isEmpty():
            for i in range(num - 1):
                queue.enqueue(queue.dequeue())
            print(queue.dequeue())



if __name__ == '__main__':
    solution = Solution()
    solution.hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7)
