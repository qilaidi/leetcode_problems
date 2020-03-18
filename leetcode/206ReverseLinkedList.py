# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/3/18

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def _reverse(node, prev = None):
            if not node:
                return prev


        return _reverse(head)
