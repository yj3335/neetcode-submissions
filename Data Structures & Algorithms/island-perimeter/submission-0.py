class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        n = len(grid)
        m = len(grid[0])

        def dfs(i,j) -> int:
            if i>=n or j>=m or i<0 or j<0 or grid[i][j] == 0:
                return 1
            if (i,j) in visited:
                return 0
            
            visited.add((i,j))
            perimeter = dfs(i,j+1)
            perimeter += dfs(i,j-1)
            perimeter += dfs(i+1, j)
            perimeter += dfs(i-1, j)

            return perimeter

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return dfs(i,j)
