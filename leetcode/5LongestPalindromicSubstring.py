# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/2/19

class Solution:
    def longestPalindrome_brute_optimize(self, s):
        def generate_palindrome(s, left, right):
            """956 ms, faster than 75.73% of Python3"""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        res = ""
        for i in range(len(s)):
            res = max(generate_palindrome(s, i, i), generate_palindrome(s, i, i+1), res, key=len)
        return res

    def longestPalindrome_(self, s):
        """没看懂"""
        length = 0
        begin = 0
        for i in range(len(s)):
            if i - length >= 0 and s[i - length:i + 1] == s[i - length:i + 1][::-1]:
                begin = i - length
                length += 1
            if i - length - 1 >= 0 and s[i - length - 1:i + 1] == s[i - length - 1:i + 1][::-1]:
                begin = i - length - 1
                length += 2
        return s[begin:begin + length]

    def longestPalindrome(self, s):
        """DP"""
        res = ""
        m = len(s)
        dp = [[0] * m for _ in range(m)]
        # dp[i][j] = true的话表示index从i到j的子串是回文串
        for i in range(m-1, -1, -1):
            for j in range(i, m):
                dp[i][j] =  s[i] == s[j] and (j - i < 2 or dp[i+1][j-1])
                if dp[i][j] and j - i + 1 > len(res):
                    res = s[i:j+1]
        return res



if __name__ == '__main__':
    test = Solution()
    print(test.longestPalindrome("babad"))
    print(test.longestPalindrome("cbbd"))
    print(test.longestPalindrome(" "))
    print(test.longestPalindrome("a"))
    print(test.longestPalindrome("ccd"))
    print(test.longestPalindrome("abadd"))
    print(test.longestPalindrome("SQQSYYSQQS"))