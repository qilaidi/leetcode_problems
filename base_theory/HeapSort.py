# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/2/13
import heapq


def heap_sort(array):
    heap = array[:]
    heapq.heapify(heap)
    for i in range(len(array)):
        array[i] = heapq.heappop(heap)
    return array

if __name__ == '__main__':
    print(heap_sort([48, 52, 13, 22, 2, 8]))
    print(heap_sort([48, 52, 13, 22, 2, 2, 8]))