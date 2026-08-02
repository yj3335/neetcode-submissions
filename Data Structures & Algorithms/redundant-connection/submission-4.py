class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = {i : i for i in range(1, len(edges)+1)}

        def helper(node):
            if parents[node] == node:
                return node 
            
            parents[node] = helper(parents[node])
            return parents[node]
        
        for src, dest in edges:
            root1 = helper(src)
            root2 = helper(dest)

            if root1 == root2:
                return [src, dest]
            else:
                parents[root1] = root2
        

            