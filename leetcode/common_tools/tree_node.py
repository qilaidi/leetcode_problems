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
                i += 1; j += 1
        return tree_node[0]

    @classmethod
    def print_tree_inorder(cls, root):
        res = []
        while root:
            if root.left:
                root = root.left
            elif not root.left:
                res.append(root)
            elif root.right:
                root = root.right
        return res
