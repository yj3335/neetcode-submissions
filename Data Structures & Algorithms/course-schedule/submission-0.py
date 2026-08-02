class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i : [] for i in range(numCourses)}
        visited = set()

        for crs, pre in prerequisites:
            graph[crs].append(pre)

        def dfs(course):
            if course in visited:
                return False
            if graph[course] == []:
                return True 
            
            visited.add(course)
            for pre in graph[course]:
                if not dfs(pre): return False
            
            visited.remove(course)
            graph[course] = []
            return True
            

        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True