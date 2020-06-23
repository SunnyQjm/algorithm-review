#!/usr/bin/env python
# coding=utf-8

###################################################################################
# 冒泡排序
###################################################################################


# 第一轮采用正向遍历的冒泡排序代码示例
def bubbleSort(A):
    n = len(A)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]


# 第一轮采用反向遍历的冒泡排序代码示例
def bubbleSort2(A):
    n = len(A)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]


if __name__ == '__main__':
    A = [5, 7, 1, 3, 6, 2, 4]
    bubbleSort(A)
    print(A, "= [1, 2, 3, 4, 5, 6, 7]")

    A = [5, 7, 1, 3, 6, 2, 4]
    bubbleSort2(A)
    print(A, "= [1, 2, 3, 4, 5, 6, 7]")
