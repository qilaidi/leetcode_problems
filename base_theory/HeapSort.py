# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/2/13
import heapq


def heap_sort(array):
    heapq.heapify(array)
    for i in range(len(array)):
        array[i] = heapq.heappop()
    return array