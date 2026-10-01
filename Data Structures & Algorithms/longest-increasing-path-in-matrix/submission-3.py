class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        cells = [[i,j,matrix[i][j]] for i in range(ROWS) for j in range(COLS)]
        cells = sorted(cells, key = lambda x : x[2], reverse=True)
        dp = [[1 for _ in range(COLS)] for _ in range(ROWS)]

        def inBounds(i,j):
            return (i >= 0 and i < ROWS and j >= 0 and j < COLS)

        for i,j,val in cells:
            for dr, dc in directions:
                nr,nc = i+dr, j+dc
                if inBounds(nr,nc) and matrix[nr][nc] > val:
                    dp[i][j] = max(dp[i][j], 1 + dp[nr][nc])
        
        ans = max([max(row) for row in dp])
        return ans