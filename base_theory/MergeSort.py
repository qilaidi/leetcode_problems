# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/2/13

def merge(array, left, mid, right):
    temp = []
    i, j = left, mid + 1
    while i <= mid and j <= right:
        if array[i] <= array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1
    if i <= mid:
        temp += array[i:mid + 1]
    if j <= right:
        temp += array[j:right + 1]
    array[left:right+1] = temp

def merge_sort(array, left, right):
    if left >= right:
        return
    mid = (left + right) >> 1
    merge_sort(array, left, mid)
    merge_sort(array, mid + 1, right)
    merge(array, left, mid, right)
    return array

if __name__ == '__main__':
    print(merge_sort([48, 52, 13, 22, 2, 8], 0, 5))
    print(merge_sort([48, 52, 13, 22, 2, 2, 8], 0, 6))