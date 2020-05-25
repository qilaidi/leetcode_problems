# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/5/25
from leetcode_problems.leetcode.common_tools.tree_node import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

