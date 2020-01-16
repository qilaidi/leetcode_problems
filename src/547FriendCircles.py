# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/1/16

class Solution:
    def findCircleNum(self, M):
        res = 0
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    res += 1
                    self.dfs(M, i, j)
        return res

    def dfs(self, M, i, j):
        if i < 0 or i == len(M) or j < 0 or j == len(M[0]):
            return
        if M[i][j] == 0:
            return
        elif M[i][j] == 1:
            self.dfs(M, i + 1, j)
            self.dfs(M, i - 1, j)
            self.dfs(M, i, j - 1)
            self.dfs(M, i, j + 1)

if __name__ == '__main__':
    M1 = [[1,1,0],
         [1,1,0],
         [0,0,1]]
    M2 = \
    [[1,1,0],
    [1,1,1],
    [0,1,1]]
    M3 = [[1, 0, 0, 1],
          [0, 1, 1, 0],
          [0, 1, 1, 1],
          [1, 0, 1, 1]]
    test = Solution()
    print(test.findCircleNum(M1))
    print(test.findCircleNum(M2))
    print(test.findCircleNum(M3))
