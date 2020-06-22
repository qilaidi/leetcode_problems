# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/2/19
import collections


class Solution:
    # def isMatch1(self, s: str, p: str) -> bool:
    #     """错的"""
    #     if not p or len(p) == 0:
    #         return (s == None or len(s) == 0)
    #     m, n = len(s) + 1, len(p) + 1
    #     dp = [[0] * n for _ in range(m)]
    #     dp[0][0] = True
    #     for j in range(2, n):
    #         dp[0][j] = dp[0][j-1] == "*" and dp[0][j-2]
    #     for j in range(1, n):
    #         for i in range(1, m):
    #             if p[j-1] in (s[i-1], "."):
    #                 dp[i][j] = dp[i-1][j-1]
    #             elif p[j-1] == "*":
    #                 dp[i][j] = dp[i][j-2] or ((s[i-1] == p[j-2]or p[j-2] == "." ) and dp[i-1][j])
    #     return not not dp[m-1][n-1]
    #
    # def isMatch1(self, s: str, p: str) -> bool:
    #     m, n, memo = len(s), len(p), collections.defaultdict(tuple)
    #     def dp(i, j):
    #         if (i, j) in memo[(i, j)]:
    #             return memo[(i, j)]
    #         if j == n:
    #             return i == m
    #         first = i < m and p[j] in (s[i], ".")
    #         if j <= n - 2 and p[j + 1] == "*":
    #             ans = dp(i, j + 2) or (first and dp(i + 1, j))
    #         else:
    #             ans = first and dp(i + 1, j + 1)
    #         memo[(i,j)] = ans
    #         return ans
    #     return dp(0, 0)

    def isMatch(self, s: str, p: str) -> bool:
        s = '#' + s
        p = '#' + p
        m, n = len(s), len(p)
        dp = [[False] * m for _ in range(n)]
        dp[0][0] = True
        for i in range(2, n):
            dp[i][0] = dp[i - 2][0] and p[i] == "*"
        for j in range(m):
            for i in range(1, n):
                if p[i] != "*":
                    dp[i][j] = (p[i] in (s[j], ".")) and dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i-2][j] or ((p[i - 1] in (s[j], ".")) and (dp[i - 1][j] or (dp[i][j - 1])))
                    # dp[i][j] = dp[i-2][j] or dp[i-1][j]
                    # if p[i-2] == s[j-1] or p[i-2] == '.':
                    #     dp[i][j] |= dp[i][j-1]
        return dp[-1][-1]

    def isMatch1(self, s, p):
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        table[0][0] = True
        for i in range(2, len(p) + 1):
            table[i][0] = table[i - 2][0] and p[i - 1] == '*'
        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != "*":
                    table[i][j] = table[i - 1][j - 1] and \
                                  (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                else:
                    table[i][j] = table[i - 2][j] or table[i - 1][j]
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        table[i][j] |= table[i][j - 1]

        return table[-1][-1]


if __name__ == '__main__':
    test = Solution()
    print(test.isMatch("aa", "a")) # False
    print(test.isMatch("aa", "a*")) # True
    print(test.isMatch("aa", "b*")) # False
    print(test.isMatch("aaa", "a*"))  # True
    print(test.isMatch("ab", ".*"))  # True
    print(test.isMatch("", ""))  # True
    print(test.isMatch("a", ""))  # False
    print(test.isMatch("", "a"))  # False
    print(test.isMatch("", "*"))  # True
    print(test.isMatch("", ".*"))  # True
    print(test.isMatch("", "a*"))  # True
    print(test.isMatch("", "."))  # False
    print(test.isMatch("mississippi", "mis*is*p*."))  # False
    print(test.isMatch("aab", "c*a*b"))  # True
    print(test.isMatch("mississippi", "mis*is*ip*."))  # True
