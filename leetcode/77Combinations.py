# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/6/11
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        if n < k:
            return []
        def helper(first, count, res):
            if count == 0:
                results.append(res[:])
                return
            for i in range(first, n + 1):
                res.append(i)
                helper(i + 1, count-1, res)
                res.pop()

        helper(1, k, [])
        return results

if __name__ == '__main__':
    test = Solution()
    print(test.combine(4, 2))
