class UnionFind:
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node):
        if node == self.parent[node]:
            return node
        
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, e in enumerate(edges):
            e.append(i) # n1, n2, weightn og_index

        edges.sort(key=lambda e : e[2])

        mst_weight = 0
        uf = UnionFind(n)

        for n1, n2, w, i in edges:
            if uf.union(n1,n2):
                mst_weight += w
        
        critical, pseudo = [], []

        for n1, n2, w, i in edges:
            # without curr
            weight = 0
            uf = UnionFind(n)

            for v1, v2, e, j in edges:
                if i != j and uf.union(v1,v2):
                    weight += e
            if max(uf.rank) != n or  weight > mst_weight:
                critical.append(i)
                continue

            #with curr 
            uf = UnionFind(n)
            uf.union(n1, n2)
            weight = w
            for v1, v2, e, j in edges:
                if uf.union(v1,v2):
                    weight += e
            if weight == mst_weight:
                pseudo.append(i)

        return [critical, pseudo]






