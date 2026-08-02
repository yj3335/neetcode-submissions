class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i : [] for i in range(numCourses)}
        for src, pre in prerequisites:
            graph[src].append(pre)
        
        visited = set()
        ans = []
        completed = set()

        def dfs(course):
            if course in visited:
                return False
            if course in completed:
                return True
            
            visited.add(course)
            for nei in graph[course]:
                if not dfs(nei): return False
            
            visited.remove(course)
            completed.add(course)
            ans.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []

        return ans
