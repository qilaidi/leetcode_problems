# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/2/2
class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set(range(1, 10)) for _ in range(9)]
        col = [set(range(1, 10)) for _ in range(9)]
        block = [set(range(1, 10)) for _ in range(9)]
        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty.append((i, j))
                else:
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    b = (i // 3) * 3 + j // 3
                    block[b].remove(val)
        def dfs(k=0):
            if k == len(empty):
                return True
            i, j = empty[k]
            b = (i // 3) * 3 + j // 3
            for val in row[i] & col[j] & block[b]:
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)
                if dfs(k+1):
                    return True
                row[i].add(val)
                col[j].add(val)
                block[b].add(val)
                board[i][j] = "."
            return False
        dfs()

