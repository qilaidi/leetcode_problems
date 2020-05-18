# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/5/18

# Input: root = [1,null,3,2,4,null,5,6]
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    @classmethod
    def generate_node(cls, a_list):
        node = [Node(x) if x is not None else None for x in a_list]
        m = len(node)
        j = 2
        for i in range(m):
            if i == 0:
                j, current_children = Node.generate_children(j, node, m)
                node[0].children = current_children
            else:
                if node[i]:
                    j, current_children = Node.generate_children(j, node, m)
                    node[i].children = current_children
        return node[0]

    @classmethod
    def generate_children(cls, j, node, m):
        current_children = []
        while j < m:
            child = node[j]
            if child == None:
                j += 1
                break
            else:
                current_children.append(child)
            j += 1
        return (j, current_children)

