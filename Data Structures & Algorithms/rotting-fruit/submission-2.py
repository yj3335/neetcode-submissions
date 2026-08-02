class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh, time = 0,0 
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        if fresh == 0:
            return 0

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while q and fresh>0:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if nr<0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    q.append((nr,nc))
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1