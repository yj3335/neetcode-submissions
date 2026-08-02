class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        visited = set()

        islands = 0

        def bfs(r, c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr+row, dc+col
                    if nr<0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc] == "0" or \
                     ((nr,nc) in visited):
                        continue
                    visited.add((nr,nc))
                    q.append((nr,nc))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and ((i,j) not in visited):
                    islands += 1
                    bfs(i,j)
        
        return islands