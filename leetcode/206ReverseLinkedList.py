# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/3/18

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def generate(self, a_list):
        list_node = [ListNode(x) for x in a_list]
        for i in range(len(list_node)):
            if i == len(list_node) - 1:
                list_node[i].next = None
            else:
                list_node[i].next = list_node[i+1]
        return list_node[0]

    @classmethod
    def print_list_node(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

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