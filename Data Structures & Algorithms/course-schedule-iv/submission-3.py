class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)

        prereqMap = {}

        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for pre in graph[crs]:
                    prereqMap[crs] |= dfs(pre)
                prereqMap[crs].add(crs)

            return prereqMap[crs]

        for i in range(numCourses):
            prereqMap[i] = dfs(i)

        res = []
        for q1, q2 in queries:
            res.append(q2 in prereqMap[q1])

        return res
        