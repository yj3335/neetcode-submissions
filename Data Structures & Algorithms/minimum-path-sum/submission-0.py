class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dp = {(m-1, n-1) : grid[m-1][n-1]}


        def dfs(r,c):
            if (r,c) in dp:
                return dp[(r,c)]

            if r == m or c == n:
                return 201
            
            val = min(dfs(r+1,c), dfs(r,c+1))
            dp[(r,c)] = grid[r][c] + val
            return dp[(r,c)]
        
        return dfs(0,0)