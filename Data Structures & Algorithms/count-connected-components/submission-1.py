class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for src, dest in edges:
            if src not in graph:
                graph[src] = []
            if dest not in graph:
                graph[dest] = []
            graph[src].append(dest)
            graph[dest].append(src)

        visited = set()
        components = 0

        def bfs(node, parent):
            if node in visited:
                return 
            
            q = deque()
            q.append([node, parent])
            visited.add(node)

            while q:
                src, parent = q.popleft()
                if src in graph:
                    for dest in graph[src]:
                        if dest not in visited and dest != parent:
                            visited.add(dest)
                            q.append([dest, src])
            

        for i in range(n):
            if i not in visited:
                bfs(i, -1)
                components += 1
            
        return components