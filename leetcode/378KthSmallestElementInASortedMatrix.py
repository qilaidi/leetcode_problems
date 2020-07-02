# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/7/2
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """这个难道不是O(2n)"""
        summary = []
        for item in matrix:
            summary += item
        return sorted(summary)[k-1]

    def kthSmallest2(self, matrix: List[List[int]], k: int) -> int:
        """2分查找，时间复杂度O(n), 空间复杂度 O(1), 最优解，官方的，还没看懂"""
        n = len(matrix)

        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left

if __name__ == '__main__':
    matrix = [
        [1, 2],
        [1, 3]
    ]
    test = Solution()
    print(test.kthSmallest(matrix, 2))

