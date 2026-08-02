class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        
        graph = {src : [] for src, dest in tickets}
        
        for src, dest in tickets:
            graph[src].append(dest)
        
        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets)+1:
                return True
            
            if src not in graph:
                return False
            
            temp = list(graph[src])
            for i, dest in enumerate(temp):
                graph[src].pop(i)
                res.append(dest)

                if dfs(dest): return True

                graph[src].insert(i, dest)
                res.pop()
            return False

        dfs("JFK")
        return res