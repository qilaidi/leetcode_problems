# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/6/2
from leetcode_problems.leetcode.common_tools import tree_node


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res, stack = [], [root]
        while stack:
            current = []
            for node in stack:
                if node:
                    res.append(node.val)
                    current.append(node.left)
                    current.append(node.right)
                else:
                    res.append(None)
            stack = current
        x = len(res) - 1
        while x >= 0:
            if res[x] is not None:
                break
            else:
                x -= 1
        res = res[:x+1]
        return str(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = eval(data) if data else None
        if data:
            data = [TreeNode(node) if node is not None else None for node in data]
            m, i, j = len(data), 0, 1
            while j < m and i < m:
                if data[i]:
                    if j < m and data[j]:
                        data[i].left = data[j]
                    j += 1
                    if j < m and data[j]:
                        data[i].right = data[j]
                    j += 1
                i += 1
        return data[0] if data else None


if __name__ == '__main__':
    null = None
    codec = Codec()
    # root = codec.deserialize("[1,2,3,null,null,4,5]")
    # root = codec.deserialize("[-1,0,1]")
    # root = codec.deserialize("[5,2,3,null,null,2,4,3,1]")
    # root = codec.deserialize("[10,9,11,8,null,null,12,7,null,null,13,6,null,null,14,5,null,null,15,4,null,null,16,3,null,null,17,2,null,null,18,1,null,null,19,0]")
    root = tree_node.TreeNode.generate_tree([10,9,11,8,null,null,12,7,null,null,13,6,null,null,14,5,null,null,15,4,null,null,16,3,null,null,17,2,null,null,18,1,null,null,19,0])
    # print((codec.serialize(root)))
    print(tree_node.TreeNode.print_tree_preorder(root))