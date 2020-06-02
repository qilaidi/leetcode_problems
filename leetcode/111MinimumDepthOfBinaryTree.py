# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/5/29
from collections import deque

from leetcode_problems.leetcode.common_tools.tree_node import TreeNode


class Solution:
    def minDepth1(self, root: TreeNode) -> int:
        "DFS 优雅的光头哥"
        if not root: return 0
        depth = list(map(self.minDepth, (root.left, root.right)))
        return 1 + (min(depth) or max(depth))

    def minDepth(self, root: TreeNode) -> int:
        """用deque效率会不会好点"""
        if not root: return 0
        min_depth, stack = 0, deque([(1, root)])
        while stack:
            min_depth, root = stack.pop()
            if root:
                if not (root.left or root.right):
                    return min_depth
                stack.insert(0, (min_depth+1, root.left))
                stack.insert(0, (min_depth+1, root.right))




if __name__ == '__main__':
    null = None
    root = TreeNode.generate_tree([3,9,20,null,null,15,7]) #2
    root1 = TreeNode.generate_tree([1,2]) #2
    root2 = TreeNode.generate_tree([1,2,3,4,5]) #2
    test = Solution()
    print(test.minDepth(root))
    print(test.minDepth(root1))
    print(test.minDepth(root2))