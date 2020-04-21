# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/3/19

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def generate(self, a_list):
        if not a_list:
            return None
        list_node = [ListNode(x) for x in a_list]
        for i in range(len(list_node)):
            if i == len(list_node) - 1:
                list_node[i].next = None
            else:
                list_node[i].next = list_node[i+1]
        return list_node[0]

    @classmethod
    def print_list_node(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res