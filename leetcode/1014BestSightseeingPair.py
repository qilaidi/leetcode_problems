# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/6/17
from typing import List


class Solution:
    def maxScoreSightseeingPair1(self, A: List[int]) -> int:
        "超时"
        res = 0
        length_a = len(A)
        for i in range(length_a, length_a - 1):
            for j in range(1, length_a):
                if i < j:
                    res = max(res, A[i] + A[j] + i - j)
        return res

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        max_i, res = A[0], 0
        length_a = len(A)
        for i in range(1, length_a):
            res = max(res, max_i + A[i] - i)
            max_i = max(max_i, A[i] + i)
        return res


if __name__ == '__main__':
    test = Solution()
    print(test.maxScoreSightseeingPair([8,1,5,2,6]))
