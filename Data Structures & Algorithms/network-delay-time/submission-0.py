class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append([v, w])
        
        visited = set()
        minHeap = [[0, k]]
        t = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(t, w1)
            for n2, w2 in graph[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, [w2+w1, n2])
        
        return t if len(visited) == n else -1