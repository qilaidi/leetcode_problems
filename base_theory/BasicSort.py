# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/2/12

"""选择排序:
    每次找最小值，放到最前面
"""
from leetcode_problems.utils.timer import timethis


@timethis
def selection_sort_extra_memory(list_a):
    """使用了额外的内存"""
    result = []
    while list_a:
        item = min(list_a)
        result.append(item)
        list_a.remove(item)
    return result

@timethis
def selection_sort(list_a):
    """不使用额外内存"""
    left = 0
    while left < len(list_a):
        index = list_a.index(min(list_a[left:]), left)
        item = list_a.pop(index)
        list_a.insert(left, item)
        left += 1
    return list_a

"""插入排序：
1。 从第一个元素开始，该元素被认为已排序
2。 取出下一个元素，在已排序的元素中从后向前扫描，按升序插入到已排序的部分
"""

def insertion_sort(list_a):
    for i in range(1, len(list_a)):
        item = list_a.pop(i)
        j = i - 1
        while j >= 0:
            if j == 0 and item <= list_a[j]:
                list_a.insert(0, item)
            elif item >= list_a[j]:
                list_a.insert(j + 1, item)
                break
            j -= 1
    return list_a

"""冒泡排序：
遍历，比较相邻元素，如果是逆序，则交换
"""

def bubble_sort(list_a):
    for x in range(len(list_a) - 1):
        for i in range(len(list_a) - 1 - x):
            if list_a[i] > list_a[i + 1]:
                list_a[i], list_a[i + 1] = list_a[i + 1], list_a[i]
    return list_a

if __name__ == '__main__':
    print(bubble_sort([48, 52, 13, 22, 2, 8]))
    print(bubble_sort([48, 52, 13, 22, 2, 2, 8]))