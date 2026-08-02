class UnionFind:
    def __init__(self, n:int) -> None:
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self,node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        
        if p1 == p2:
            return False
        
        if self.rank[p1] >= self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        
        emailToIndex = {}

        for i,e in enumerate(accounts):
            for a in e[1:]:
                if a not in emailToIndex:
                    emailToIndex[a] = i
                else:
                    uf.union(i, emailToIndex[a])
        
        nodeToEmails = {}

        for key, value in emailToIndex.items():
            p = uf.find(value)
            if p not in nodeToEmails:
                nodeToEmails[p] = []
            nodeToEmails[p].append(key)
        
        ans = []
        for key, value in nodeToEmails.items():
            n = accounts[key][0]
            ans.append([n] + sorted(value))
        
        return ans





