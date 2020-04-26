# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/4/21
from leetcode_problems.leetcode.common_tools.list_node import ListNode


class Solution:
    def mergeTwoLists_recursive_extra_space(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(-1)
        def merge(h1, h2, res):
            if not h1:
                res.next = h2
            elif not h2:
                res.next = h1
            elif h1.val < h2.val:
                res.next = h1
                merge(h1.next, h2, res.next)
            else:
                res.next = h2
                merge(h1, h2.next, res.next)
            return res
        merge(l1, l2, result)
        return result.next

    def mergeTwoLists_recursive(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
        return l1 if l1.val <= l2.val else l2

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(-1)
        cur = result
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return result.next


if __name__ == '__main__':
    l1 = ListNode.generate([1, 2, 4])
    l2 = ListNode.generate([1, 3, 4])
    test = Solution()
    print(ListNode.print_list_node(test.mergeTwoLists(l2, l1)))