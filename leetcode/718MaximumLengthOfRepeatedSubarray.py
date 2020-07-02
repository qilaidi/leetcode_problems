# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/07/01
from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m, n = len(A) + 1, len(B) + 1
        dp = [[0] * m for _ in range(n)]
        res = 0
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j-1] + 1 if A[i-1] == B[j-1] else 0
                res = max(res, dp[i][j])
        return res


if __name__ == '__main__':
    test = Solution()
    print(test.findLength([1,2,3,2,1], [3,2,1,4,7])) #3