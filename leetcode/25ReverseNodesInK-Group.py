# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/3/31
from leetcode_problems.leetcode.common_tools.list_node import ListNode


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr, count = head, 0
        while curr and count < k:
            curr = curr.next
            count += 1
        if count == k:
            curr = self.reverseKGroup(curr, k)
            # curr 当前最后
            # head 当前最前
            for _ in range(count):
                temp = head.next
                head.next = curr
                curr = head
                head = temp
            head = curr
        return head

    def reverseKGroup_(self, head: ListNode, k: int) -> ListNode:
        l, node = 0, head
        while node:
            l += 1
            node = node.next
        if k <= 1 or l < k:
            return head
        node, cur = None, head
        # node 指向 tail
        # cur 指向 head
        # 先处理本层，把下一段的头下探到下一层，最后之间head.next指向返回的头
        for _ in range(k):
            nxt = cur.next
            cur.next = node
            node = cur
            cur = nxt
        head.next = self.reverseKGroup(cur, k)
        return node

