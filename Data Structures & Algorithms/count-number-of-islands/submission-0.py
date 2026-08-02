class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid), len(grid[0])
        visited = set()

        def island(i,j) -> None:
            if i >= rows or j >= cols or i<0 or j<0 or ((i,j) in visited) \
                or grid[i][j] == "0":
                return
            
            visited.add((i,j))
            island(i, j-1)
            island(i, j+1)
            island(i-1, j)
            island(i+1, j)

        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != "0" and (i,j) not in visited:
                    ans += 1
                    island(i,j)
        
        return ans