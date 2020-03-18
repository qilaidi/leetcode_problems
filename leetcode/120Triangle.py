# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/1/20

class Solution:
    def minimumTotal(self, triangle):
        res = 0
        for i in range(len(triangle)):
            if i - 2 >= 0:
                res += min(triangle[i][i-1], triangle[i][i], triangle[i][i-2])
            elif i - 1 >= 0:
                res += min(triangle[i][i-1], triangle[i][i])
            else:
                res += triangle[i][i]
        return res


if __name__ == '__main__':
    triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
    triangle1 = [[-1],[2,3],[1,-1,-3]]
    test = Solution()
    print(test.minimumTotal(triangle)) #11
    print(test.minimumTotal(triangle1)) #-1