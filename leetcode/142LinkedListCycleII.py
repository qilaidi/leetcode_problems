# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/3/31
from leetcode_problems.leetcode.common_tools.list_node import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        memo = []
        while head:
            if head in memo:
                return head
            memo.append(head)
            head = head.next
        return None

    def detectCycle_double_(self, head: ListNode) -> ListNode:
        walker, runner = head, head
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if runner == walker:
                break
        else:
            return None
        while head != walker:
            head = head.next
            walker = walker.next
        return head


