#!/usr/bin/env python
# coding=utf-8

###################################################################################
# 快速排序
###################################################################################


def quickSort(A):
    def quickSortHelper(A, l, r):
        if l >= r:
            return
        i, j, pivotIndex = l, r, l
        while i < j:
            while i < j and A[j] >= A[pivotIndex]:
                j -= 1
            while i < j and A[i] <= A[pivotIndex]:
                i += 1
            A[i], A[j] = A[j], A[i]
        A[i], A[pivotIndex] = A[pivotIndex], A[i]
        quickSortHelper(A, l, i - 1)
        quickSortHelper(A, i + 1, j)

    quickSortHelper(A, 0, len(A) - 1)


if __name__ == '__main__':
    A = [5, 7, 1, 3, 6, 2, 4]
    quickSort(A)
    print(A, "= [1, 2, 3, 4, 5, 6, 7]")