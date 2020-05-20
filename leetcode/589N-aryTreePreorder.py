# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/5/20
from typing import List

from leetcode_problems.leetcode.common_tools.Node import Node


class Solution:
    def preorder_recursive(self, root: 'Node') -> List[int]:
        def helper(root, res):
            if root:
                res.append(root.val)
                for x in root.children:
                    helper(x, res)
            return res
        return helper(root, [])

    def preorder(self, root: 'Node') -> List[int]:
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack += reversed(node.children)
        return res



if __name__ == '__main__':
    test = Solution()
    root = Node.generate_node([1,None,3,2,4,None,5,6]) # [1,3,5,6,2,4]
    print(test.preorder(root))