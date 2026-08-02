class Solution:
    def validPalindrome(self, s: str) -> bool:
        def reverse(temp: str) -> bool:
            left, right = 0, len(temp)-1
            while left<right:
                if temp[left] != temp[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        if reverse(s):
            return True
        
        for i in range(len(s)):
            temp = s[:i] + s[i+1:]
            if reverse(temp):
                return True
        
        return False
        