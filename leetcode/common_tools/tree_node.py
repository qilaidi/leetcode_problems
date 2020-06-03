# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/4/29

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def generate_tree(cls, a_list):
        if not a_list:
            return None
        tree_node = [TreeNode(x) if x is not None else None for x in a_list]
        m, i, j = len(tree_node), 0, 1
        while i < m and j < m:
            if tree_node[i]:
                if j < m and tree_node[j]:
                    tree_node[i].left = tree_node[j]
                j += 1
                if j < m and tree_node[j]:
                    tree_node[i].right = tree_node[j]
                j += 1
            i += 1
        return tree_node[0]

    @classmethod
    def print_tree_preorder(cls, root):
        res, stack = [], [root]
        while stack:
            current = []
            for node in stack:
                if node:
                    res.append(node.val)
                    current.append(node.left)
                    current.append(node.right)
                else:
                    res.append(None)
            stack = current
        x = len(res) - 1
        while x >= 0:
            if res[x] is not None:
                break
            else:
                x -= 1
        res = res[:x + 1]
        return res
