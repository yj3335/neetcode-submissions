class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)

        visited = set()
        components = 0

        def bfs(node):
            if node in visited:
                return 
            
            q = deque()
            q.append(node)
            visited.add(node)

            while q:
                src = q.popleft()
                for dest in graph[src]:
                    if dest not in visited:
                        visited.add(dest)
                        q.append(dest)
            

        for i in range(n):
            if i not in visited:
                bfs(i)
                components += 1
            
        return components