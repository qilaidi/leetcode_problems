# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/2/19

class Solution:
    def validPalindrome_1(self, s: str) -> bool:
        """Time Limit Exceeded"""
        if s == s[::-1]:
            return True
        for index in range(len(s)):
            new_s = s[:index]+s[index+1:]
            if new_s == new_s[::-1]:
                return True
        return False

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return s[left:right] == s[left:right][::-1] or s[left+1:right+1] == s[left+1:right+1][::-1]
            left += 1
            right -= 1
        return True



if __name__ == '__main__':
    test = Solution()
    print(test.validPalindrome("aba"))
    print(test.validPalindrome("abca"))
    print(test.validPalindrome("pidbliassaqozokmtgahluruufwbjdtayuhbxwoicviygilgzduudzgligyviciowxbhuyatdjbwfuurulhagtmkozoqassailbdip"))