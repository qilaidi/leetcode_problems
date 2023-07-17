from typing import Optional

from leetcode.common_tools.list_node import ListNode


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        res = head
        prev = head
        while head:
            if head.val == val:
                if prev == head:
                    prev = head.next
                    res = prev
                else:
                    prev.next = head.next
            else:
                if prev != head:
                    prev = head
            head = head.next
        return res

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        head.next = self.removeElements(head.next, val)
        if head.val == val:
            return head.next
        else:
            return head


if __name__ == '__main__':
    test = Solution()
    print(ListNode.print_list_node(test.removeElements(ListNode.generate([1, 2, 6, 3, 4, 5, 6]), 6)))
    assert ListNode.print_list_node(test.removeElements(ListNode.generate([1, 2, 6, 3, 4, 5, 6]), 6)) == [1, 2, 3, 4, 5]
    assert ListNode.print_list_node(test.removeElements(ListNode.generate([]), 1)) == []
    assert ListNode.print_list_node(test.removeElements(ListNode.generate([7, 7, 7, 7]), 7)) == []
