class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self, words) -> None:
        self.root = TrieNode()
        for w in words:
            cur = self.root
            for c in w:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.endOfWord = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie(dictionary).root
        cache = {len(s) : 0}

        def dfs(index):
            if index in cache:
                return cache[index]
            
            res = 1 + dfs(index+1)
            cur = trie
            for j in range(index, len(s)):
                if s[j] not in cur.children:
                    break
                cur = cur.children[s[j]]
                if cur.endOfWord:
                    res = min(res, dfs(j+1))

            cache[index] = res
            return res
        
        return dfs(0)


