class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # r + c 
        negDiag = set() # r - c 

        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(row): #for each row we try to place the queen in a col
            if row == n:
                copy = ["".join(r) for r in board]
                res.append(copy)
                return 
            
            for c in range(n):
                if c in col or (row + c) in posDiag or (row - c) in negDiag:
                    continue
                
                board[row][c] = "Q"
                col.add(c)
                posDiag.add(row + c)
                negDiag.add(row - c)

                backtrack(row+1)

                board[row][c] = "."
                col.remove(c)
                posDiag.remove(row + c)
                negDiag.remove(row - c)
        backtrack(0)
        return res