class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
            if n == 1:
                return [0]

            graph = defaultdict(list)
            for src, dest in edges:
                graph[src].append(dest)
                graph[dest].append(src)
            
            edges_cnt = {}
            q = deque() #leaves
        
            for node, neighbors in graph.items():
                if len(neighbors) == 1:
                    q.append(node)
                edges_cnt[node] = len(neighbors)
            
            while q:
                if n <= 2:
                    return list(q)
                for _ in range(len(q)):
                    node = q.popleft()
                    n -= 1
                    for nei in graph[node]:
                        edges_cnt[nei] -= 1
                        if edges_cnt[nei] == 1:
                            q.append(nei)


            