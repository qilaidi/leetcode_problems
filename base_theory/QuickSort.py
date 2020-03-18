# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/2/13

def partition_1(a, begin, end):
    pivot = end
    counter = begin
    for i in range(begin, end):
        if a[i] < a[pivot]:
            a[i], a[counter] = a[counter], a[i]
            counter += 1
    a[pivot], a[counter] = a[counter], a[pivot]
    return counter


def partition(a, begin, end):
    pivot = end
    cur = begin
    while cur < pivot:
        if a[cur] > a[pivot]:
            item = a.pop(cur)
            pivot -= 1
            a.insert(pivot + 1, item)
        else:
            cur += 1
    return pivot

def quick_sort(list_a, begin, end):
    if end <= begin:
        return
    pivot = partition(list_a, begin, end)
    quick_sort(list_a, begin, pivot - 1)
    quick_sort(list_a, pivot + 1, end)
    return list_a

if __name__ == '__main__':
    print(quick_sort([48, 52, 13, 22, 2, 8], 0, 5))
    print(quick_sort([48, 52, 13, 22, 2, 2, 8], 0, 6))