class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific_set = set()
        atlantic_set = set()

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def helper(r,c,prev_height,visited):
            if r<0 or c<0 or r>=rows or c>=cols or ((r,c) in visited):
                return
            
            if heights[r][c] < prev_height:
                return 

            visited.add((r,c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                helper(nr, nc, heights[r][c], visited)
            
        for col in range(cols):
            helper(0, col, heights[0][col], pacific_set)
            helper(rows-1, col, heights[rows-1][col], atlantic_set)

        for row in range(rows):
            helper(row, 0, heights[row][0], pacific_set)
            helper(row, cols-1, heights[row][cols-1], atlantic_set)

        ans = []
        for r,c in pacific_set:
            if (r,c) in atlantic_set:
                ans.append([r,c])

        return ans

        
             