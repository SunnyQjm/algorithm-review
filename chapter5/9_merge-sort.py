#!/usr/bin/env python
# coding=utf-8

###################################################################################
# 归并排序
###################################################################################


def mergeSort(A):
    def merge(A, l, m, r):
        leftHalf, rightHalf, i, j, k = A[l: m + 1], A[m + 1: r + 1], 0, 0, l
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] <= rightHalf[j]:
                A[k], i, k = leftHalf[i], i + 1, k + 1
            else:
                A[k], j, k = rightHalf[j], j + 1, k + 1
        while i < len(leftHalf):
            A[k], i, k = leftHalf[i], i + 1, k + 1
        while j < len(rightHalf):
            A[k], j, k = rightHalf[j], j + 1, k + 1

    def mergeSortHelper(A, l, r):
        if l >= r:
            return
        m = (l + r) // 2
        mergeSortHelper(A, l, m)
        mergeSortHelper(A, m + 1, r)
        merge(A, l, m, r)

    mergeSortHelper(A, 0, len(A) - 1)


if __name__ == '__main__':
    A = [5, 7, 1, 3, 6, 2, 4]
    mergeSort(A)
    print(A, "= [1, 2, 3, 4, 5, 6, 7]")
