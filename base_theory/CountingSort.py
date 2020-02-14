# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/2/13
import collections


def counting_sort(arr, max_value):
    new_arr = []
    dic = collections.defaultdict(int)
    for item in arr:
        dic[item] += 1
    for i in range(max_value):
        while dic.get(i, 0) > 0:
            new_arr.append(i)
            dic[i] -= 1
    return new_arr

if __name__ == '__main__':
    print(counting_sort([48, 52, 13, 22, 2, 8], 52))
    print(counting_sort([48, 52, 13, 22, 2, 2, 8], 52))
