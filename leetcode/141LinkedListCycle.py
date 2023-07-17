# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/3/26
from leetcode.common_tools.list_node import ListNode


class Solution:
    def hasCycle_normal(self, head: ListNode) -> bool:
        memo = []
        while head:
            if head in memo:
                return True
            memo.append(head)
            head = head.next
        return False

    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        walker = runner = head
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if runner == walker:
                return True
        return False

    def hasCycle(self, head: ListNode) -> bool:
        if not (head and head.next):
            return False
        fast, slow = head.next, head
        while fast.next:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return True





