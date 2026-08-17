class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: 
            return True
        if not t or len(s) > len(t):
            return False

        left, right = 0, 0
        while right < len(t) and left < len(s):
            if s[left] == t[right]:
                left += 1
            right += 1
        return left == len(s)