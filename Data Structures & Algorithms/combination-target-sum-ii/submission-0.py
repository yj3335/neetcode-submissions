class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(index, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if index >= len(candidates) or total > target:
                return
            
            cur.append(candidates[index])
            dfs(index+1, cur, total + candidates[index])

            cur.pop()
            while index<len(candidates)-1 and candidates[index] == candidates[index+1]:
                index += 1
            dfs(index+1, cur, total)
        
        dfs(0, [], 0)
        return res