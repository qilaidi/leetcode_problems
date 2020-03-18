# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/1/8

class Solution:
    def longestCommonSubsequence_1(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # 初始化第一行第一列 增加0行0列表示其中一个字符为""的情况
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1) + 1, len(text2) + 1
        dp = [[0] * m for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]



if __name__ == '__main__':
    test = Solution()
    print(test.longestCommonSubsequence("abcde", "ace")) #3
    print(test.longestCommonSubsequence("abc", "abc")) #3
    print(test.longestCommonSubsequence("abc", "def")) #0
    print(test.longestCommonSubsequence("bsbininm", "jmjkbkjkv")) #1
