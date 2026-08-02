class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        cache = {}
        #backtracking and memoization 
        def backtracking(index):
            if index == len(s):
                return [""]
            if index in cache:
                return cache[index]

            res = []
            for j in range(index, len(s)):
                w = s[index:j+1]
                if w not in wordDict:
                    continue
                strings = backtracking(j+1)
                if not strings:
                    continue
                for substr in strings:
                    sentence = w
                    if substr:
                        sentence += " " + substr
                    res.append(sentence)
            cache[index] = res
            return res 
        return backtracking(0)

