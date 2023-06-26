from typing import List

from leetcode.common_tools.tree_node import TreeNode


class Solution:
    """默写好几遍了"""
    def inorderTraversal1(self, root):
        path = []
        self.helper(root, path)
        return path

    def helper(self, root, path):
        if root:
            self.helper(root.left, path)
            path.append(root.val)
            self.helper(root.right, path)
        return path

    def inorder_traversal(self, root):
        path = []
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return path
            node = stack.pop()
            path.append(node.val)
            root = node.right
        return path

    def inorder_traversal_more_faster(self, root):
        """找了个最快的，结果为啥我提交就不是最快了，还没上面递归的快s"""
        path = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            path.append(root.val)
            root = root.right
        return path

    def inorderTraversal2_recursive(self, root: TreeNode) -> List[int]:
        """2刷递归"""
        def helper(root, res):
            if root:
                helper(root.left, res)
                res.append(root.val)
                helper(root.right, res)
            return res
        res = []
        helper(root, res)
        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """2刷栈"""
        res, stack = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if not node.left:
                res.append(node.val)
                stack.append(node.right)
            else:
                stack.append(node)
                stack.append(node.left)
        return res






if __name__ == '__main__':
    test = Solution()
    root = TreeNode.generate_tree([1,None,2,3])
    print(test.inorderTraversal(root))