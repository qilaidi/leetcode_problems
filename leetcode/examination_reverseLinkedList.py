class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def reverseList(self, head):
        while head:
            prev_node = head.next
            if prev_node:
                prev_node.next = head
                head = prev_node
        return head

if __name__ == '__main__':
    test = Solution()
    test.reverseList()

