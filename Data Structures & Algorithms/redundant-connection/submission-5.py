class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parent = [i for i in range(N+1)]
        rank = [1] * (N+1)

        def find(node):
            if node == parent[node]:
                return node
            
            parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            p1, p2 = find(node1), find(node2)

            if p1==p2:
                return False
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return True
        
        for n1, n2 in edges:
            if not union(n1,n2):
                return [n1, n2]
            

