class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        cache = {len(s) : 0}

        def dfs(index):
            if index in cache:
                return cache[index]
            
            res = 1 + dfs(index+1) #skip cur character 
            for j in range(index, len(s)):
                if s[index:j+1] in dictionary:
                    res = min(res, dfs(j+1))
            cache[index] = res
            return res
        
        return dfs(0)