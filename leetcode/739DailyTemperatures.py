# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/6/11
from typing import List


class Solution:
    def dailyTemperatures1(self, T: List[int]) -> List[int]:
        """超时"""
        res, d = [], {}
        length = len(T)
        for i in range(length):
            for k, v in d.items():
                if d[k][1] is False:
                    d[k][2] = d[k][2] + 1
                if T[i] > d[k][0]:
                    d[k][1] = True
            if i not in d:
                d[i] = [T[i], False, 0]
        for k, v in d.items():
            if d[k][1] is True:
                res.append(v[2])
            elif d[k][1] is False:
                res.append(0)
        return res

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        length = len(T)
        res = [0] * length
        stack = []
        for i in range(length):
            while stack and (T[i] > T[stack[-1]]):
                finished = stack.pop()
                res[finished] = i - finished
            stack.append(i)
        return res



if __name__ == '__main__':
    test = Solution()
    print(test.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])) # [1, 1, 4, 2, 1, 1, 0, 0]

