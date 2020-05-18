# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/5/18
from typing import List

from leetcode_problems.leetcode.common_tools.tree_node import TreeNode


class Solution:
    def preorderTraversal_recursive(self, root: TreeNode) -> List[int]:
        """1刷递归"""
        """执行用时 :28 ms, 在所有 Python3 提交中击败了98.38%的用户"""

        def helper(root, res):
            if root:
                res.append(root.val)
                helper(root.left, res)
                helper(root.right, res)
            return res
        return helper(root, [])

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        while root or stack:
            while root:
                res.append(root.val)
                stack.append(root.right)
                root = root.left
            root = stack.pop()
        return res




if __name__ == '__main__':
    test = Solution()
    root = TreeNode.generate_tree([1,None,2,3])
    print(test.preorderTraversal(root))