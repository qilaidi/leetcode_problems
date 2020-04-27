# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/4/27

class Solution:
    def isValid(self, s: str) -> bool:
        """执行用时 :32 ms, 在所有 Python3 提交中击败了91.52%的用户"""
        stack = []
        for x in s:
            if x == "(":
                stack.append(")")
            elif x == "[":
                stack.append("]")
            elif x == "{":
                stack.append("}")
            elif stack != [] and x == stack[-1]:
                stack.pop()
            else:
                return False
        return not stack

if __name__ == '__main__':
    test = Solution()
    print(test.isValid("([)]"))
    print(test.isValid("(]"))
    print(test.isValid("()[]{}"))
    print(test.isValid("{[]}"))
    print(test.isValid("()"))
    print(test.isValid(")"))