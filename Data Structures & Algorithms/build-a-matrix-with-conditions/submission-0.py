class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def dfs(src, graph, visited, path, order):
            if src in path:
                return False
            if src in visited:
                return True
            
            path.add(src)
            visited.add(src)
            for nei in graph[src]:
                if not dfs(nei, graph, visited, path, order):
                    return False

            path.remove(src)
            order.append(src)
            return True

        def topo_sort(arr):
            graph = defaultdict(list)
            for src, dest in arr:
                graph[src].append(dest)
            
            visited, path = set(), set()
            order = []

            for src in range(1, k+1):
                if not dfs(src, graph, visited, path, order):
                    return []
            
            return order[::-1]

        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)

        if not row_order or not col_order:
            return []
        
        val_to_row = {n:i for i, n in enumerate(row_order)}
        val_to_col = {n:i for i, n in enumerate(col_order)}

        res = [[0]*k for _ in range(k)]

        for src in range(1, k+1):
            r, c = val_to_row[src], val_to_col[src]
            res[r][c] = src
        
        return res