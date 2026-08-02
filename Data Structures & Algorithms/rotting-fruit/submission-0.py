class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        fresh = 0

        def addEdge(i,j):
            nonlocal fresh
            if i<0 or j<0 or i>=rows or j>=cols or grid[i][j] == 0 or ((i,j) in visited):
                return
            q.append((i,j))
            visited.add((i,j))
            fresh -= 1
            
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
        
        minutes = 0
        
        while q and fresh > 0:
            minutes += 1
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = 2
                addEdge(row+1, col)
                addEdge(row-1, col)
                addEdge(row, col+1)
                addEdge(row, col-1)
                
        return minutes if fresh==0 else -1
        