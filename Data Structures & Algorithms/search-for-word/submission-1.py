class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        directions = [[1,0], [-1,0], [0, 1], [0, -1]]

        def dfs(index, r, c):
            if index == len(word):
                return True
            
            if (r<0 or r>=rows or
                c<0 or c>=cols or 
                word[index] != board[r][c] or 
                (r,c) in visited): 
                return False

            visited.add((r,c))
            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if dfs(index+1, nr, nc): return True

            visited.remove((r,c))
            return False
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(0, r, c): return True
        
        return False