class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        mp = {}
        for c in s:
            mp[c] = mp.get(c,0)+1
        
        for c in t:
            if c in mp:
                mp[c] -= 1

        for val in mp.values():
            if val > 0:
                return False

        return True