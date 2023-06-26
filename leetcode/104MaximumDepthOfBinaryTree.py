# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/5/29
from typing import Optional

from leetcode.common_tools.tree_node import TreeNode


class Solution:
    def maxDepth1(self, root: TreeNode) -> int:
        "DFS"
        def helper(root, res, level):
            return max(helper(root.left, max(res, level), level+1), helper(root.right, max(res, level), level+1)) if root else res
        return helper(root, 0, 1)

    def maxDepth2(self, root: TreeNode) -> int:
        "BFS 不优雅"
        res, stack = 0, [root] if root else []
        while stack:
            res += 1
            current_nodes = []
            for node in stack:
                if node.left:
                    current_nodes.append(node.left)
                if node.right:
                    current_nodes.append(node.right)
            stack = current_nodes
        return res

    def maxDepth3(self, root: TreeNode) -> int:
        "DFS 优雅de光头哥"
        return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0

    def maxDepth(self, root: TreeNode) -> int:
        "BFS 优雅"
        max_depth, stack = 0, [(1, root)] if root else []
        while stack:
            depth, root = stack.pop()
            if root:
                max_depth = max(depth, max_depth)
                stack.append((depth+1, root.left))
                stack.append((depth+1, root.right))
        return max_depth

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [root]
        res = 0
        flag = 0
        while stack:
            ss = len(stack)
            while ss > 0:
                node = stack.pop(0)
                ss -= 1
                if node:
                    flag = 1
                    stack.append(node.left)
                    stack.append(node.right)
            if flag:
                res += 1
                flag = 0
        return res


if __name__ == '__main__':
    null = None
    root = TreeNode.generate_tree([3,9,20,null,null,15,7])
    root1 = TreeNode.generate_tree([1,2])
    test = Solution()
    print(test.maxDepth(root))
    print(test.maxDepth(root1))