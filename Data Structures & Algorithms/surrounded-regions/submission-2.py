class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(i,j):
            if i<0 or j<0 or i>=rows or j>=cols or board[i][j] != "O":
                return 
            
            board[i][j] = "T"
            for dr, dc in directions:
                dfs(i+dr, j+dc)

        for c in range(cols):
            dfs(0, c)
            dfs(rows-1, c)

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols-1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"