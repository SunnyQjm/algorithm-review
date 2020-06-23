#!/usr/bin/env python
# coding=utf-8

###################################################################################
# 插入排序
###################################################################################


def insertSort(A):
    n = len(A)
    for i in range(1, n):
        curIndex = i
        for j in range(curIndex - 1, -1, -1):
            if A[j] > A[curIndex]:
                A[j], A[curIndex], curIndex = A[curIndex], A[j], j
            else:
                break


if __name__ == '__main__':
    A = [5, 7, 1, 3, 6, 2, 4]
    insertSort(A)
    print(A, "= [1, 2, 3, 4, 5, 6, 7]")
