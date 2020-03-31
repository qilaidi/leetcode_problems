# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/3/26
from leetcode_problems.leetcode.common_tools.list_node import ListNode


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
        walker = head
        runner = head.next
        while walker != runner:
            if not runner or not runner.next:
                return False
            walker = walker.next
            runner = runner.next.next
        return True

