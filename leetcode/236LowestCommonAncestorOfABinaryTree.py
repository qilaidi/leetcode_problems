# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/6/3
from collections import deque

from leetcode_problems.leetcode.common_tools.tree_node import TreeNode


class Solution:
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """执行用时 :80 ms, 在所有 Python3 提交中击败了92.73%的用户"""
        ans = None
        def helper(node):
            if not node: return False
            left = helper(node.left)
            right = helper(node.right)
            if (left and right) or ((left or right) and ((node.val == p.val) or (node.val == q.val))):
                nonlocal ans
                ans = node
            return left or right or ((node.val == p.val) or (node.val == q.val))
        helper(root)
        return ans

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {root.val: None}
        ans = set()
        stack = deque([root])
        while p.val not in parents or q.val not in parents:
            node = stack.pop()
            if node.left:
                parents[node.left.val] = node
                stack.append(node.left)
            if node.right:
                parents[node.right.val] = node
                stack.appendleft(node.right)
        while p:
            ans.add(p.val)
            p = parents[p.val]
        while q.val not in ans:
            q = parents[q.val]
        return q


if __name__ == '__main__':
    null = None
    root = TreeNode.generate_tree([3,5,1,6,2,0,8,null,null,7,4])
    p = TreeNode.generate_tree([5,6,2,null,null,7,4])
    q = TreeNode.generate_tree([1,0,8])
    test = Solution()
    ans = test.lowestCommonAncestor(root, p, q)
    print(ans)
