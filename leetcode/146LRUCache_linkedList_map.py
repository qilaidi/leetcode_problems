# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/2/11

class LinkedNode(object):
    def __init__(self):
        self.key, self.value = 0, 0
        self.prev, self.next = None, None

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head, self.tail = LinkedNode(), LinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        node = self.cache.get(key, None)
        if not node:
            return -1
        self._move_to_head(node)
        return node.value

    def put(self, key, value):
        node = self.cache.get(key, None)
        if not node:
            node = LinkedNode()
            node.key = key
            node.value = value
            if self.size == self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
            elif self.size < self.capacity:
                self.size += 1
        else:
            node.value = value
            self._remove_node(node)
        self._add_node(node)
        self.cache[key] = node

    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next = node
        node.next.prev = node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        node = self.tail.prev
        self._remove_node(node)
        return node

if __name__ == '__main__':
    test = LRUCache(2)
    test.put(2, 1)
    test.put(1, 1)
    test.put(2, 3)
    test.put(4, 1)
    print(test.get(1))
    print(test.get(2))
