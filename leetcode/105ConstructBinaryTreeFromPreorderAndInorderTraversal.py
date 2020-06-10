# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/6/10
from typing import List

from leetcode_problems.leetcode.common_tools.tree_node import TreeNode


class Solution:
    def buildTree1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            current_root = TreeNode(preorder.pop(0))
            current_root.left = self.buildTree(preorder,inorder[0:inorder.index(current_root.val)])
            current_root.right = self.buildTree(preorder,inorder[inorder.index(current_root.val)+1:])
            return current_root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder: return None
        index = inorder.index(preorder.pop(0))
        current_root = TreeNode(inorder[index])
        current_root.left = self.buildTree(preorder,inorder[0:index])
        current_root.right = self.buildTree(preorder,inorder[index+1:])
        return current_root



#     3
#    / \
#   9  20
#     /  \
#    15   7
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]

if __name__ == '__main__':
    test = Solution()
    print(TreeNode.print_tree_preorder(test.buildTree([3,9,20,15,7], [9,3,15,20,7])))
