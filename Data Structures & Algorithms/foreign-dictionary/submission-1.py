class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c : set() for word in words for c in word}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
            
        visited = {} # c : visited or not
        res = []

        def dfs(c):
            if c in visited:
                return visited[c]
            
            visited[c] = True 

            for nei in graph[c]:
                if dfs(nei): return True

            visited[c] = False
            res.append(c)

        for c in graph:
            if dfs(c) : return ""
        
        res.reverse()
        return "".join(res)
        