# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/2/19
import re


class Solution:
    def isPalindrome_1(self, s: str) -> bool:
        """44ms"""
        new_s = ""
        for ch in s:
            if ch.isalpha() or ch.isnumeric():
                new_s += ch
        new_s = new_s.lower()
        return new_s == new_s[::-1]

    def isPalindrome(self, s: str) -> bool:
        """32ms"""
        s = re.sub("[^a-zA-Z0-9]", "", s).lower()
        return s == s[::-1]

if __name__ == '__main__':
    test = Solution()
    print(test.isPalindrome("A man, a plan, a canal: Panama"))
    print(test.isPalindrome("race a car"))