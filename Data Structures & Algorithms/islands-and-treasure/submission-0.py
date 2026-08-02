class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def addEdge(i,j):
            if i<0 or j<0 or i>=rows or j>=cols or grid[i][j] == -1 or ((i,j) in visited):
                return 
            q.append((i,j))
            visited.add((i,j))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))

        dist = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist
                addEdge(row+1, col)
                addEdge(row-1, col)
                addEdge(row, col+1)
                addEdge(row, col-1)
            dist += 1
        