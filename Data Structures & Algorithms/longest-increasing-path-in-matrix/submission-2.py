class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        dp = {}
        res = 0

        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            ans = 1
            for dr, dc in directions:
                nr, nc = dr + i, dc + j
                if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and matrix[i][j] < matrix[nr][nc]:
                    ans = max(ans, 1 + dfs(nr,nc))
            dp[(i,j)] = ans
            return ans
        
        for i in range(ROWS):
            for j in range(COLS):
                res = max(res, dfs(i,j))
        
        return res
