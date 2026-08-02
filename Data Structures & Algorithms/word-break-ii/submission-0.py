class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        #backtracking
        wordDict = set(wordDict)
        
        cur = []
        res = []

        def backtracking(index):
            if index == len(s):
                res.append(" ".join(cur))
                return
            
            for j in range(index, len(s)):
                w = s[index:j+1]
                if w in wordDict:
                    cur.append(w)
                    backtracking(j+1)
                    cur.pop()
        backtracking(0)
        return res
        

