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
        m = len(tree_node)
        for i in range(m):
            if tree_node[i]:
                if i + 1 < m:
                    tree_node[i].left = tree_node[i+1]
                if i + 2 < m:
                    tree_node[i].right = tree_node[i+2]
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
