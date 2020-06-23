#!/usr/bin/env python
# coding=utf-8

###################################################################################
# 选择排序
###################################################################################


def selectSort(A):
    n = len(A)
    for i in range(n - 1):
        minValueIndex = i
        for j in range(i + 1, n):
            if A[j] < A[minValueIndex]:
                minValueIndex = j
        A[i], A[minValueIndex] = A[minValueIndex], A[i]


if __name__ == '__main__':
    A = [5, 7, 1, 3, 6, 2, 4]
    selectSort(A)
    print(A, "= [1, 2, 3, 4, 5, 6, 7]")
