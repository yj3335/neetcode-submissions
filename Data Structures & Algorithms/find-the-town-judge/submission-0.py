class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = [[0] * n for _ in range(n)]
        for pair in trust:
            i,j = pair
            graph[i-1][j-1] = 1

        for i in range(n):
            sum = 0
            for j in range(n):
                sum += graph[i][j]
            if sum == 0:
                colSum = 0
                for j in range(n):
                    colSum += graph[j][i]
                if colSum == n-1:
                    return i+1
        
        return -1