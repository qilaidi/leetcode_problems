# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/3/18
from leetcode_problems.leetcode.common_tools.list_node import ListNode


class Solution:
    def reverseList_recursive(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        node = self.reverseList_recursive(head.next)
        head.next.next = head
        head.next = None
        return node

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

if __name__ == '__main__':
    head = ListNode.generate([1, 2, 3, 4, 5])
    test = Solution()
    node = test.reverseList(head)
    print(ListNode.print_list_node(node))