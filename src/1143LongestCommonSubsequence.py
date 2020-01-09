# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/1/8

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

if __name__ == '__main__':
    test = Solution()
    print(test.longestCommonSubsequence("abcde", "ace")) #3
    print(test.longestCommonSubsequence("abc", "abc")) #3
    print(test.longestCommonSubsequence("abc", "def")) #0
    print(test.longestCommonSubsequence("bsbininm", "jmjkbkjkv")) #1
