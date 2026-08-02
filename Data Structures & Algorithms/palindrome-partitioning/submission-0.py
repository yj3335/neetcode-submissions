class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(index):
            if index >= len(s):
                res.append(part[:])
                return
            
            for j in range(index, len(s)):
                if self.isPalindrome(s, index, j):
                    part.append(s[index:j+1])
                    dfs(j+1)
                    part.pop()
        
        dfs(0)
        return res
    
    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left + 1, right - 1

        return True