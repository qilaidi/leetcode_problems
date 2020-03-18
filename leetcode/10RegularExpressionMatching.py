# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/2/19
import collections


class Solution:
    def isMatch_a(self, s: str, p: str) -> bool:
        if not p or len(p) == 0:
            return (s == None or len(s) == 0)
        m, n = len(s) + 1, len(p) + 1
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = True
        for j in range(2, n):
            dp[0][j] = dp[0][j-1] == "*" and dp[0][j-2]
        for j in range(1, n):
            for i in range(1, m):
                if p[j-1] in (s[i-1], "."):
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i][j-2] or ((s[i-1] == p[j-2]or p[j-2] == "." ) and dp[i-1][j])
        return dp[m-1][n-1]

    def isMatch(self, s: str, p: str) -> bool:
        m, n, memo = len(s), len(p), collections.defaultdict(tuple)
        def dp(i, j):
            if (i, j) in memo[(i, j)]:
                return memo[(i, j)]
            if j == n:
                return i == m
            first = i < m and p[j] in (s[i], ".")
            if j <= n - 2 and p[j + 1] == "*":
                ans = dp(i, j + 2) or (first and dp(i + 1, j))
            else:
                ans = first and dp(i + 1, j + 1)
            memo[(i,j)] = ans
            return ans
        return dp(0, 0)


if __name__ == '__main__':
    test = Solution()
    print(test.isMatch("aa", "a"))
    print(test.isMatch("aa", "a*"))






