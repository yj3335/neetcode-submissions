class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        posDiag = set() # r + c
        negDiag = set() # r - c 

        res = 0
        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                nonlocal res
                res += 1
                return
            
            for c in range(n):
                if c in cols or (row+c) in posDiag or (row-c) in negDiag:
                    continue
                
                board[row][c] = "Q"
                cols.add(c)
                posDiag.add(row+c)
                negDiag.add(row-c)

                backtrack(row+1)

                board[row][c] = "."
                cols.remove(c)
                posDiag.remove(row+c)
                negDiag.remove(row-c)
        backtrack(0)
        return res


