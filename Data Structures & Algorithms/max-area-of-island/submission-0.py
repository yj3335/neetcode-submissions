class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()
        maxArea = 0

        def bfs(r,c) -> int:
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            area = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if nr<0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc] == 0 or \
                        ((nr,nc) in visited):
                        continue
                    visited.add((nr,nc))
                    q.append((nr,nc))
                    area += 1
            
            return area


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and ((i,j) not in visited):
                    a = bfs(i,j)
                    maxArea = max(maxArea,a)
        
        return maxArea