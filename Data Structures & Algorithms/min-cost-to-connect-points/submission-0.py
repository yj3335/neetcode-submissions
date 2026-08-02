class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = {i : [] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                diff = abs(x1-x2)+abs(y2-y1)
                graph[i].append([diff, j])
                graph[j].append([diff, i])
        
        res = []
        total = 0
        visited = set()
        minHeap = [[0, 0]]

        while len(visited)<n:
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            visited.add(i)
            total += cost

            for neiCost, nei in graph[i]:
                if nei not in visited:
                    heapq.heappush(minHeap, [neiCost, nei])
        
        return total