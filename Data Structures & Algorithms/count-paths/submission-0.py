class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n # n cols, 1 row used , remaining m-1 

        for i in range(m-1):
            newRow = [1] * n
            for j in range(n-2, -1, -1): # we know n-1 col will always be 1
                newRow[j] = newRow[j+1] + row[j] #right value is j+1 and down value is row[j] as newrow is on top of row
            row = newRow
        
        return row[0]