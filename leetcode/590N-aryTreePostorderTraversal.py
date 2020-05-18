# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/5/18
from typing import List

from leetcode_problems.leetcode.common_tools.Node import Node


class Solution:
    def postorder_recursive(self, root: 'Node') -> List[int]:
        def helper(root, res):
            if root:
                for x in root.children:
                    helper(x, res)
                res.append(root.val)
            return res
        return helper(root, [])

    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack, res = [root], []
        while stack:
            root = stack.pop()
            stack += root.children
            res.append(root.val)
        return list(reversed(res))


if __name__ == '__main__':
    test = Solution()
    root = Node.generate_node([1,None,3,2,4,None,5,6])
    print(test.postorder(root))