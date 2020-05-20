# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/5/20
from typing import List

from leetcode_problems.leetcode.common_tools.Node import Node


class Solution:
    def levelOrder_1(self, root: 'Node') -> List[List[int]]:
        stack, res = [[root]], []
        while stack:
            node = stack.pop(0)
            if any(node):
                current_res, current_children = [], []
                for x in node:
                    current_res.append(x.val)
                    current_children += x.children
                stack.append(current_children)
                res.append(current_res)
        return res

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        stack, res = [root], []
        while any(stack):
            res.append([x.val for x in stack])
            stack = [child for node in stack for child in node.children if child]
        return res

if __name__ == '__main__':
    test = Solution()
    null = None
    root = Node.generate_node([])
    print(type(test.levelOrder_1(root)))
    print(test.levelOrder(root))