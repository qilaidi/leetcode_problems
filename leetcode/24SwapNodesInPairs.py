# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/3/19
from leetcode_problems.leetcode.common_tools.list_node import ListNode


class Solution:
    def swapPairs_dfs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        first_node = head
        second_node = head.next
        new_head = self.swapPairs(second_node.next)
        second_node.next = first_node
        first_node.next = new_head
        return second_node

    def swapPairs(self, head: ListNode) -> ListNode:
        result = ListNode(-1)
        result.next = head
        prev_node = result
        while head and head.next:

            first_node = head
            second_node = head.next

            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            prev_node = first_node
            head = first_node.next

        return result.next

if __name__ == '__main__':
    head = ListNode.generate([1, 2, 3, 4, 5, 6, 7, 8])
    test = Solution()
    node = test.swapPairs(head)
    print(ListNode.print_list_node(node))