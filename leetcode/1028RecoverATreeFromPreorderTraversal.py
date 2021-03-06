# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/6/18
import collections



# Input: "1-2--3--4-5--6--7"
# Output: [1,2,5,3,4,6,7]
# Input: "1-2--3---4-5--6---7"
# Output: [1,2,5,3,null,6,null,4,null,7]
# Input: "1-401--349---90--88"
# Output: [1,401,null,349,88,90]
from leetcode_problems.leetcode.common_tools.tree_node import TreeNode


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        S += "$"
        stack = []
        current_key, prev_key, current_value, current_children = "", "", "", []
        for ch in S:
            if ch == "$":
                level = prev_key.count("-")
                while stack and (level < stack[-1][0]):
                    while (current_children == []) or current_children[-1][0] == stack[-1][0]:
                        current_children.append(stack.pop())
                    if len(current_children) == 2:
                        stack[-1][1].left = current_children.pop()[1]
                        stack[-1][1].right = current_children.pop()[1]
                    elif len(current_children) == 1:
                        stack[-1][1].left = current_children.pop()[1]
                stack.append((level, TreeNode(int(current_value))))
            if ch == '-':
                current_key += "-"
                if current_value:
                    level = prev_key.count("-")
                    while stack and (level < stack[-1][0]):
                        while (current_children == []) or current_children[-1][0] == stack[-1][0]:
                            current_children.append(stack.pop())
                        if len(current_children) == 2:
                            stack[-1][1].left = current_children.pop()[1]
                            stack[-1][1].right = current_children.pop()[1]
                        elif len(current_children) == 1:
                            stack[-1][1].left = current_children.pop()[1]
                    stack.append((level, TreeNode(int(current_value))))
                    current_value = ""
                    prev_key = ""
            elif ch.isdigit():
                if current_key:
                    prev_key = current_key
                    current_key = ""
                current_value += ch
        while len(stack) > 1:
            while (current_children == []) or current_children[-1][0] == stack[-1][0]:
                current_children.append(stack.pop())
            if len(current_children) == 2:
                stack[-1][1].left = current_children.pop()[1]
                stack[-1][1].right = current_children.pop()[1]
            elif len(current_children) == 1:
                stack[-1][1].left = current_children.pop()[1]
        return stack[0][1]

if __name__ == '__main__':
    test = Solution()
    print(test.recoverFromPreorder("10-7--8"))

