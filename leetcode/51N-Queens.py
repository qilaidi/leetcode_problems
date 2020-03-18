class Solution:
    def solveNQueens_1(self, n):
        queen_board = []
        def generate_queens(col, pie ,na):
            current_row = len(col)
            if current_row == n:
                queen_board.append(col)
                return
            for x in range(n):
                if x not in col and current_row + x not in pie and current_row - x not in na:
                    generate_queens(col + [x], pie + [current_row + x], na + [current_row - x])
        generate_queens([], [], [])
        return [["." * x + "Q" + "." * (n - 1 - x) for x in solution] for solution in queen_board]

    def solveNQueens_2(self, n):
        """2"""
        queen_board = []
        def generate_queens(col, pie, na):
            row = len(col)
            if row == n:
                queen_board.append(col)
            for x in range(n):
                if x not in col and row + x not in pie and row - x not in na:
                    generate_queens(col+[x], pie+[row+x], na+[row-x])
        generate_queens([], [], [])
        return [["."*x+"Q"+"."*(n-x-1) for x in solution] for solution in queen_board]

    def solveNQueens(self, n):
        def generate_queens(col, pie, na):
            row = len(col)
            if row == n:
                queen_board.append(col)
            for i in range(n):
                if i not in col and row + i not in pie and row - i not in na:
                    generate_queens(col+[i], pie+[row+i], na+[row-i])
        queen_board = []
        generate_queens([], [], [])
        print(queen_board)
        return [["."*i+"Q"+"."*(n-i-1) for i in solution] for solution in queen_board]

if __name__ == '__main__':
    test = Solution()
    print(test.solveNQueens(4))