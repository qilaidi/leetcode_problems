# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/5/25
from leetcode_problems.leetcode.common_tools.tree_node import TreeNode


class Solution:
    def isValidBST1(self, root: TreeNode) -> bool:
        def helper(root, res):
            if root:
                helper(root.left, res)
                res.append(root.val)
                helper(root.right, res)
            if res:
                current = res[0]
                for v in res[1:]:
                    if current >= v:
                        return False
                    current = v
                return True
        if not root:
            return True
        return helper(root, [])

    def isValidBST2(self, root: TreeNode) -> bool:
        def helper(root, low, high):
            if not root:
                return True
            if low < root.val < high:
                return helper(root.left, low, min(root.val, high)) and \
                       helper(root.right, max(root.val, low), high)
            else:
                return False
        return helper(root, float("-inf"), float("inf"))

    def isValidBST(self, root: TreeNode) -> bool:
        prev_val = float("-inf")
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            curr_val = root.val
            if curr_val <= prev_val:
                return False
            prev_val = curr_val
            root = root.right
        return True




if __name__ == '__main__':
    null = None
    test = Solution()
    root = TreeNode.generate_tree([1, 1])
    root1 = TreeNode.generate_tree([2,1,3])
    root2 = TreeNode.generate_tree([5,1,4,null,null,3,6])
    root3 = TreeNode.generate_tree([])
    root4 = TreeNode.generate_tree([10,5,15,null,null,6,20])
    res = test.isValidBST(root)
    res1 = test.isValidBST(root1)
    res2 = test.isValidBST(root2)
    res3= test.isValidBST(root3)
    res4= test.isValidBST(root4)
    print(res)
    print(res1)
    print(res2)
    print(res3)
    print(res4)